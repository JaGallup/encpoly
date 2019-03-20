import sphinx_rtd_theme


project = "encpoly"
copyright = "2019 Já hf"

master_doc = "index"
exclude_patterns = ["_build", ".DS_Store"]
default_role = "py:obj"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    "navigation_depth": 4,
}
html_last_updated_fmt = "%d %B %Y"
html_use_index = False
html_domain_indices = False
html_copy_source = False
html_show_sphinx = False
pygments_style = "lovelace"
