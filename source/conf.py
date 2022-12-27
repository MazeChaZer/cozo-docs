# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'The Cozo Database Manual'
copyright = '2022, Ziyang Hu'
author = 'Ziyang Hu'
release = '0.4.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx',
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []

add_function_parentheses = False
add_module_names = False
latex_show_urls = 'footnote'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['override.css']
html_title = "CozoDB 0.4"
# html_baseurl = '/'
