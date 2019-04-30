import sys, os
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'node-irc'
copyright = u'2011, Martyn Smith'
version = '2.1'

release = '2.1'

exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'node-ircdoc'
latex_documents = [
  ('index', 'node-irc.tex', u'node-irc Documentation',
   u'Martyn Smith', 'manual'),
]
man_pages = [
    ('index', 'node-irc', u'node-irc Documentation',
     [u'Martyn Smith'], 1)
]
