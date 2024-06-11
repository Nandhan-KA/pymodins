
project = 'pymodins'
copyright = '2024, Nandhan K'
author = 'Nandhan K'
release = '2.1.1'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_context = {
    'google_site_verification': 'w6WcqTlHnT1hyck_miLc4L2PWN7i6p2xa78lEK65cME'  # Add your Google site verification code here
}

def setup(app):
    app.add_config_value('google_site_verification', 'w6WcqTlHnT1hyck_miLc4L2PWN7i6p2xa78lEK65cME', 'html')
    app.connect('html-page-context', add_meta_tags)

def add_meta_tags(app, pagename, templatename, context, doctree):
    context['metatags'] = f"""
        <meta name="google-site-verification" content="{app.config.google_site_verification}">
    """