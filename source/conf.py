# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'pymodins'
copyright = '2024, Nandhan K'
author = 'Nandhan K'
release = '2.1.6'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Path to the logo image
html_logo = '_static/Logo.png'  # Ensure the logo image is in the source/_static directory

html_context = {
    'google_site_verification': 'w6WcqTlHnT1hyck_miLc4L2PWN7i6p2xa78lEK65cME',
    'ms_site_verification': '5A494790FAEAB28B72F0FED494093DA2'
}

def setup(app):
    app.add_config_value('google_site_verification', 'w6WcqTlHnT1hyck_miLc4L2PWN7i6p2xa78lEK65cME', 'html')
    app.add_config_value('ms_site_verification', '5A494790FAEAB28B72F0FED494093DA2', 'html')
    app.connect('html-page-context', add_meta_tags)

def add_meta_tags(app, pagename, templatename, context, doctree):
    context['metatags'] = f"""
        <meta name="google-site-verification" content="{app.config.google_site_verification}">
        <meta name="msvalidate.01" content="{app.config.ms_site_verification}">
    """
