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
    'sphinxcontrib.mermaid',
    'sphinx.ext.graphviz',  # For diagrams (optional)
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'  # You mentioned you want the Alabaster theme
html_static_path = ['_static']

# Favicon and logo settings
html_logo = '_static/Logo.png'  # Ensure the logo image is present here
html_favicon = '_static/favicon.ico'  # Add a favicon if available

# Theme-specific options for Alabaster
html_theme_options = {
    'description': 'Pymodins: Python Module Installer',
    'github_user': 'Nandhan-ka',
    'github_repo': 'pymodins',
    'show_powered_by': False,
    'sidebar_width': '250px',
}

# Add custom static files like JS and CSS
html_js_files = ['animation.js']
html_css_files = ['custom.css']

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
