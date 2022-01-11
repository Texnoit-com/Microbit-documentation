# -- Project information -----------------------------------------------------

project = 'Microbit-ru'
copyright = '2022, Maxim Bekurin, Read the Docs, Inc. & contributors'
author = 'Maxim Bekurin'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

language = 'ru'

exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'analytics_id': 'G-XXXXXXXXXX',  
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': 'view',
    'style_nav_header_background': '#2980B9',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_static_path = ['_static']