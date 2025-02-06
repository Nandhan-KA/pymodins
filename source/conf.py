# Configuration file for the Sphinx documentation builder.
# -- Project information -----------------------------------------------------
project = 'pymodins'
copyright = '2025, Nandhan K'
author = 'Nandhan K'
release = '2.2.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx_panels',
    'sphinx_tabs.tabs',
    'sphinx_copybutton',
    'sphinxcontrib.mermaid'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'  # Changed to Alabaster
html_static_path = ['_static']

# Favicon and logo settings
html_logo = '_static/Logo.png'  # Ensure the logo image is present here
html_favicon = '_static/favicon.ico'  # Add a favicon if available

# Theme-specific options for Alabaster
html_theme_options = {
    'description': 'Pymodins ',
    'github_user': 'Nandhan-KA',  # Optional: GitHub username
    'github_repo': 'pymodins',  # Optional: GitHub repository name
    'sidebar_width': '300px',
    'page_width': '80%',  # Adjust the page width if needed
    'show_powered_by': False,  # Hide the "powered by" text
    'logo': 'Logo.png',  # You can adjust the logo path
    'favicon': 'favicon.ico',  # You can adjust the favicon path
}

# Code block styling
pygments_style = 'friendly'
pygments_dark_style = 'native'

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
