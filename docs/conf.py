import os
import sys
import time

import guzzle_sphinx_theme

sys.path.insert(0, os.path.abspath(".."))
import crotal
from crotal import version


master_doc = "index"

project = "Crotal"

version = release = version.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    ]

primary_domain = 'py'
default_role = 'py:obj'

autodoc_member_order = "bysource"
autoclass_content = "both"

# Without this line sphinx includes a copy of object.__init__'s docstring
# on any class that doesn't define __init__.
# https://bitbucket.org/birkenfeld/sphinx/issue/1337/autoclass_content-both-uses-object__init__
autodoc_docstring_signature = False

coverage_skip_undoc_in_source = True

coverage_ignore_functions = [
    # various modules
    "doctests",
    "main",

    # parse_qs_bytes should probably be documented but it's complicated by
    # having different implementations between py2 and py3.
    "parse_qs_bytes",
]

# HACK: sphinx has limited support for substitutions with the |version|
# variable, but there doesn't appear to be any way to use this in a link
# target.
# http://stackoverflow.com/questions/1227037/substitutions-inside-links-in-rest-sphinx
# The extlink extension can be used to do link substitutions, but it requires a
# portion of the url to be literally contained in the document.  Therefore,
# this link must be referenced as :current_tarball:`z`

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# On RTD we can't import sphinx_rtd_theme, but it will be applied by
# default anyway.  This block will use the same theme when building locally
# as on RTD.
if not on_rtd:
    html_translator_class = 'guzzle_sphinx_theme.HTMLTranslator'
    html_theme_path = guzzle_sphinx_theme.html_theme_path()
    html_theme = 'guzzle_sphinx_theme'

    # Register the theme as an extension to generate a sitemap.xml
    extensions.append("guzzle_sphinx_theme")

    # Guzzle theme options (see theme.conf for more information)
    html_theme_options = {
        # Set the name of the project to appear in the sidebar
        "project_nav_name": "Crotal",
    }
