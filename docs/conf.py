# -*- coding: utf-8 -*-
from pkg_resources import get_distribution


# sphinx settings
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'repoze.sphinx.autointerface',
]

source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'
html_last_updated_fmt = '%b %d, %Y'
todo_include_todos = True
autodoc_member_order = 'bysource'

# general substitutions
project = 'senic CryptoYAML'
copyright = '2016'
version = release = get_distribution('senic.cryptoyaml').version
