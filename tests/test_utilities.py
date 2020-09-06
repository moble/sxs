import pytest

import sxs

from .conftest import environment_context


@pytest.mark.parametrize("persistent", (True, False))
def test_sxs_directory(persistent):
    with pytest.raises(ValueError):
        sxs.utilities.sxs_directory("cacheconfig", persistent=persistent)


@pytest.mark.parametrize(
    ("directory_type", "persistent"),
    (
        pytest.param("config", True, id="config persistent"),
        pytest.param("cache", True, id="cache persistent"),
        pytest.param("config", False, id="config temporary"),
        pytest.param("cache", False, id="cache temporary"),
    ),
)
@pytest.mark.forked
def test_sxs_directory_cache_env(directory_type, persistent, tmp_path):
    import pathlib
    import os
    sxs.utilities.sxs_directory.cache_clear()
    with environment_context(**{f"SXS{directory_type.upper()}DIR": str(tmp_path)}):
        sxs_dir = sxs.utilities.sxs_directory(directory_type, persistent=persistent)
    assert isinstance(sxs_dir, pathlib.Path)
    if persistent:
        assert str(tmp_path) == str(sxs_dir)
    else:
        assert str(tmp_path) != str(sxs_dir)
    assert sxs_dir.exists()
    d = sxs_dir / "sub"
    d.mkdir()
    assert d.exists()
    p = d / "hello.txt"
    p.write_text("hi there")
    assert p.exists()
    assert p.read_text() == "hi there"


@pytest.mark.parametrize(
    ("directory_type",),
    (
        pytest.param("config", id="config"),
        pytest.param("cache", id="cache"),
    ),
)
@pytest.mark.forked
def test_sxs_directory_unwritable(directory_type, tmp_path):
    import os
    import stat
    d = tmp_path / "unwritable"
    d.mkdir(mode=0o000)
    assert d.exists()
    assert d.is_dir()
    assert stat.filemode(d.stat().st_mode) == "d---------"
    assert not os.access(str(d), os.W_OK)
    with environment_context(**{"HOME": str(d), f"SXS{directory_type.upper()}DIR": str(d)}):
        sxs.utilities.sxs_directory.cache_clear()
        with pytest.warns(UserWarning):
            sxs_dir = sxs.utilities.sxs_directory(directory_type, persistent=True)
        assert ".sxs" not in str(sxs_dir), (str(sxs_dir), str(d))
        sxs_config_dir = sxs.utilities.sxs_directory("config", persistent=True)
        assert str(sxs_config_dir) in str(sxs_dir)