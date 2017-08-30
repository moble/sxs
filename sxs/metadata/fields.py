"""List of metadata fields, along with various attributes for use in catalog web page

"""

metadata_fields = [
    {
        'name': 'name',
        'title': r'Name',
        'tooltip': 'Primary short name by which this simulation is known',
        'type': 'text',
        'visible': True,
        'width': '110'
    },
    {
        'name': 'simulation_name',
        'title': r'Full name',
        'tooltip': 'Full simulation name',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'alternative_names',
        'title': r'Other names',
        'tooltip': 'Other names by which this run has been referenced',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'keywords',
        'title': r'Keywords',
        'tooltip': 'Keywords to qualitatively identify this simulation',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'point_of_contact_email',
        'title': r'Contact',
        'tooltip': 'Point-of-contact email for this waveform.  Usually the person having placed the waveform into the repository.',
        'type': 'text',
        'visible': True,
        'itemTemplate': 'sxs_format_email'
    },
    {
        'name': 'authors_emails',
        'title': r'Authors\' emails',
        'tooltip': 'Researchers who contributed to the generation of this waveform',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'simulation_bibtex_keys',
        'title': r'Sim bib keys',
        'tooltip': 'ADS BibTeX keys for this simulation',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'code_bibtex_keys',
        'title': r'Code bib keys',
        'tooltip': 'ADS BibTeX keys for the evolution code',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'initial_data_bibtex_keys',
        'title': r'ID bib keys',
        'tooltip': 'ADS BibTeX keys for the initial data',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'quasicircular_bibtex_keys',
        'title': r'QC bib keys',
        'tooltip': 'ADS BibTeX keys for eccentricity reduction',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'initial_data_type',
        'title': r'ID type',
        'tooltip': 'Initial-data type',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'initial_separation',
        'title': r'$\mathrm{sep}_{\mathrm{ini}}',
        'tooltip': 'Initial separation',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'initial_orbital_frequency',
        'title': r'$\Omega_{\mathrm{orb}\ \mathrm{ini}}$',
        'tooltip': 'Initial orbital frequency',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'initial_adot',
        'title': r'$\dot{a}_{\mathrm{ini}}$',
        'tooltip': 'initial rate of change of separation',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'object1',
        'title': r'Object 1',
        'tooltip': 'Type of object 1 (BH or NS)',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'object2',
        'title': r'Object 2',
        'tooltip': 'Type of object 2 (BH or NS)',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'initial_ADM_energy',
        'title': r'$E_{\mathrm{ADM}}$',
        'tooltip': 'ADM energy measured in the initial data',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'initial_ADM_linear_momentum',
        'title': r'$\vec{P}_{\mathrm{ADM}}$',
        'tooltip': 'ADM linear momentum measured in the initial data',
        'type': 'vector',
        'visible': False,
    },
    {
        'name': 'initial_ADM_angular_momentum',
        'title': r'$\vec{L}_{\mathrm{ADM}}$',
        'tooltip': 'ADM angular momentum measured in the initial data',
        'type': 'vector',
        'visible': False,
    },
    {
        'name': 'initial_mass1',
        'title': r'$M_{\mathrm{ini}, 1}$',
        'tooltip': 'Initial mass of object 1',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'initial_mass2',
        'title': r'$M_{\mathrm{ini}, 2}$',
        'tooltip': 'Initial mass of object 2',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'initial_dimensionless_spin1',
        'title': r'$\vec{chi}_{\mathrm{ini}, 1}$',
        'tooltip': 'Initial dimensionless spin of object 1',
        'type': 'vector',
        'visible': False,
    },
    {
        'name': 'initial_dimensionless_spin2',
        'title': r'$\vec{chi}_{\mathrm{ini}, 2}$',
        'tooltip': 'Initial dimensionless spin of object 2',
        'type': 'vector',
        'visible': False,
    },
    {
        'name': 'initial_position1',
        'title': r'$\vec{x}_{\mathrm{ini}, 1}$',
        'tooltip': 'Initial position of object 1',
        'type': 'vector',
        'visible': False,
    },
    {
        'name': 'initial_position2',
        'title': r'$\vec{x}_{\mathrm{ini}, 2}$',
        'tooltip': 'Initial position of object 2',
        'type': 'vector',
        'visible': False,
    },
    {
        'name': 'relaxed_measurement_time',
        'title': r'$t_{\mathrm{rel}}$',
        'tooltip': 'Time at which "relaxed" quantities are measured',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'relaxed_mass1',
        'title': r'$M_{\mathrm{rel}, 1}$',
        'tooltip': 'Mass of object 1 after relaxation',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'relaxed_mass2',
        'title': r'$M_{\mathrm{rel}, 2}$',
        'tooltip': 'Mass of object 2 after relaxation',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'relaxed_dimensionless_spin1',
        'title': r'$\vec{chi}_{\mathrm{rel}, 1}$',
        'tooltip': 'Dimensionless spin of object 1 after relaxation',
        'type': 'vector',
        'visible': False,
    },
    {
        'name': 'relaxed_dimensionless_spin2',
        'title': r'$\vec{chi}_{\mathrm{rel}, 2}$',
        'tooltip': 'Dimensionless spin of object 2 after relaxation',
        'type': 'vector',
        'visible': False,
    },
    {
        'name': 'relaxed_position1',
        'title': r'$\vec{x}_{\mathrm{rel}, 1}$',
        'tooltip': 'Position of object 1 after relaxation',
        'type': 'vector',
        'visible': False,
    },
    {
        'name': 'relaxed_position2',
        'title': r'$\vec{x}_{\mathrm{rel}, 2}$',
        'tooltip': 'Position of object 2 after relaxation',
        'type': 'vector',
        'visible': False,
    },
    {
        'name': 'relaxed_orbital_frequency',
        'title': r'$\Omega_{\mathrm{orb}\ \mathrm{rel}}$',
        'tooltip': 'Orbital frequency after relaxation',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'relaxed_eccentricity',
        'title': r'$e_{\mathrm{rel}}$',
        'tooltip': 'Eccentricity after relaxation',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'relaxed_mean_anomaly',
        'title': r'$M_{\mathrm{rel}}$',
        'tooltip': 'Mean anomaly after relaxation',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'merger_time',
        'title': r'$t_{\mathrm{merg}}$',
        'tooltip': 'Merger time',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'number_of_orbits',
        'title': r'$N_{\mathrm{orb}}$',
        'tooltip': 'Number of orbits from beginning of simulation to merger',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'final_time',
        'title': r'$t_{\mathrm{fin}}$',
        'tooltip': 'Final time',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'remnant_mass',
        'title': r'$M_{\mathrm{rem}}$',
        'tooltip': 'Mass of remnant object',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'remnant_dimensionless_spin',
        'title': r'$\vec{\chi}_{\mathrm{rem}}$',
        'tooltip': 'Dimensionless spin of remnant object',
        'type': 'vector',
        'visible': False,
    },
    {
        'name': 'remnant_velocity',
        'title': r'$\vec{v}_{\mathrm{rem}}$',
        'tooltip': 'Velocity of remnant object',
        'type': 'vector',
        'visible': False,
    },
    {
        'name': 'disk_mass',
        'title': r'$M_{\mathrm{disk}}$',
        'tooltip': 'Mass of any remaining disk',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'ejecta_mass',
        'title': r'$M_{\mathrm{ejecta}}',
        'tooltip': 'ejecta mass',
        'type': 'float',
        'visible': False,
    },
    {
        'name': 'spec_revisions',
        'title': r'SpEC revisions',
        'tooltip': 'SpEC revisions',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'spells_revision',
        'title': r'SPELLS revision',
        'tooltip': 'SPELLS revision',
        'type': 'text',
        'visible': False,
    },
    {
        'title': 'Files',
        'type': 'text',
        'filtering': False,
        'visible': True,
        'itemTemplate': 'sxs_format_downloads'
    }
]
