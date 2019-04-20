# -*- coding: utf-8 -*-
#
# How to in AIMMS documentation build configuration file, created by
# sphinx-quickstart on Wed Dec 13 15:09:51 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from sphinx.builders import html as builders
from sphinx.util import logging
#import pdb
import subprocess
#spellcheck
if os.name == 'nt':
	import platform
	# import ssl
	# import urllib

# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
	'sphinx.builders.linkcheck']

#```
#This next if-then-else tries to import advanced extensions
#Please mind the spelling extension is only available for 32bits Python (2 or 3) currently (2019-04-01)
#```
SpellCheck_Please = False # ------------------------------------------------------------------------------------> To activate spellchecking (make spelling)



if os.name == 'nt' and platform.architecture()[0]=='64bit' and SpellCheck_Please:

		#pdb.set_trace()
		try:
			import sphinxcontrib.spelling
			success = 1
		except ImportError ,e:
			success = 0
			pass	
			
		if success:	
			#Import spelling extension
			extensions.append('sphinxcontrib.spelling')
			
			#Retrieve the one and only spelling exception central file 
			import requests
			url = "https://gitlab.aimms.com/Arthur/unified-spelling_word_list_filename/raw/master/spelling_wordlist.txt"
			#to debug, please comment the following line
			requests.packages.urllib3.disable_warnings()
			r = requests.get(url,verify=False)
			with open('spelling_wordlist.txt','wb') as f:
			  f.write(r.content)
		else:
			
			logger = logging.getLogger(__name__)
			logger.info("\nIf you would like to use the Spell Checker, please make sure to install the extension by running ``python -m pip install sphinxcontrib.spelling``, and to run Python 32bits\n")

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'ContentIndex'

title = 'AIMMS How-To'

# General information about the project.
project = title
copyright = u'2019, AIMMS'
author = u'AIMMS'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1'
# The full version, including alpha/beta/rc tags.
release = u'0'

# includes these texts at the end of all source .rsts, helpful for using repetitive replacements 

rst_epilog = """
.. |date| date:: %B, %Y

.. |time| date:: %H:%M

Last Updated: |date|
"""

# .. |set| image:: /resources/icons/Set.png

# .. |par| image:: /resources/icons/Parameter.png

# .. |var| image:: /resources/icons/Variable.png

# .. |cons| image:: /resources/icons/Constraint.png

# .. |index| image:: /resources/icons/index.png

# .. |sp| image:: /resources/icons/StringParameter.png

# .. |doc| image:: /resources/icons/Documentation.png

# .. |aimmsIcon| image:: /resources/icons/favicon.png
#                :scale: 15 %


# include these texts at the beginning of all source .rsts, use only for HTML builds to update last updated date. 

# rst_prolog = """
# Last Updated on |date|
# """

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

#html_theme = 'sphinx_materialdesign_theme'
#html_theme_path = ["."]

html_theme = 'sphinx_rtd_theme'

html_logo = 'Resources/images/aimms-logo.png' 

html_title = title

html_use_index = True
html_show_sourcelink = False

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_theme_options = {
    'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # 'vcs_pageview_mode': '',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
 #   'includehidden': True,
 #   'titles_only': False
 }


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# if builds on GitLab (a Linux machine), force "Edit on Gitlab" not to be shown :)
if os.name != 'nt':
    Display_edit_on_gitlab = False
else:   
    Display_edit_on_gitlab = True

# removed reference to theme.css as it no longer exists     
html_context = {
    'css_files': ['_static/Hacks.css', '_static/copycode.css'],
    "display_gitlab": Display_edit_on_gitlab, # Integrate Gitlab
    "gitlab_user": "aimms/customer-support", # Username
    "gitlab_repo": "aimms-how-to", # Repo name
    "gitlab_version": "master", # Version
    "conf_py_path": "", # Path in the checkout to the docs root
    "suffix": ".rst",
}

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'localtoc.html',
#         #'relations.html',  # needs 'show_related': True theme option to display
#         #'sourcelink.html',
#         'searchbox.html'
#     ]
# }
html_favicon = "_static/favicon.png"
#rst_prolog = "\n.. include:: ../special.rst\n"

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'HowToinAIMMSdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'HowToinAIMMS.tex', title,
     u'AIMMS User Support Team', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'howtoinaimms', title,
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, title, title,
     author, title, 'One line description of project.',
     'Miscellaneous'),
]

# if builds on GitLab (a Linux machine), force todos not to be shown :)
if os.name != 'nt':
	todo_include_todos = False
else:
	#To check any broken links 
	nitpicky = True


# Generate redirects from old URLs

redirects_file = "WebSite_Redirection_Mapping/redirection_map.txt"

"""
    sphinxcontrib.redirects
    ~~~~~~~~~~~~~~~~~~~~~~~
    Generate redirects for moved pages when using the HTML builder.
    See the README file for details. https://github.com/sphinx-contrib/redirects/blob/master/sphinxcontrib/redirects/__init__.py
    :copyright: Copyright 2017 by Stephen Finucane <stephen@that.guru>
    :license: BSD, see LICENSE for details.
"""

TEMPLATE = """<html>
  <head><meta http-equiv="refresh" content="0; url=/%s"/></head>
</html>
"""

def generate_redirects(app):
    
    logger = logging.getLogger(__name__)
    
    #only if not on Linux (Gitlab computers)
    if os.name == 'nt':
        #Generates the mapping file out of Git logs by launching a batch script, Assuming you have git installed on your computer... 
        try:
            subprocess.call([r'WebSite_Redirection_Mapping\\Run_generate_redirection_map.bat'], stdout=open(os.devnull, 'wb'))
            logger.info("Redirection map file has been written in WebSite_Redirection_Mapping\\redirection_map_full.txt")
        except:
            logger.warning("Website Mapping file couldn't be generated. Please debug the generate_redirects() function in conf.py. Redirection mapping is ignored.")
            pass
            return
        
    #pdb.set_trace()
    path = os.path.join(app.srcdir, app.config.redirects_file)
    if not os.path.exists(path):
        app.info("Could not find redirects file at '%s'" % path)
        return

    in_suffix = app.config.source_suffix.keys()[0]

    # TODO(stephenfin): Add support for DirectoryHTMLBuilder
    if not type(app.builder) == builders.StandaloneHTMLBuilder:
        app.warn("The 'sphinxcontrib-redirects' plugin is only supported "
                 "by the 'html' builder. Skipping...")
        return
    
    
    logger.info("Redirection Generation has started..." )
    redirects_counter = 0
    with open(path) as redirects:
        for line in redirects.readlines():
            from_path, to_path = line.rstrip().split('\t')
            redirects_counter += 1
            #To have an overview of all the redirections generated, enable logs :)
            #logger.info("Redirecting '%s' to '%s'" % (from_path, to_path))
            
            from_path = from_path.replace(in_suffix, '.html')
            to_path_prefix = '..%s' % os.path.sep * (
                len(from_path.split(os.path.sep)) - 1)
            to_path = to_path_prefix + to_path.replace(in_suffix, '.html')

            redirected_filename = os.path.join(app.builder.outdir, from_path)
            redirected_directory = os.path.dirname(redirected_filename)
            if not os.path.exists(redirected_directory):
                os.makedirs(redirected_directory)

            with open(redirected_filename, 'w') as f:
                f.write(TEMPLATE % to_path)
                
    logger.info("Redirection Generation has finished successfully! With %i redirections" % redirects_counter )
    
# The setup function here is picked up by sphinx at each build. You may input any cool change here, like syntax highlighting or redirects
def setup(sphinx):
	
    # Import the AIMMSLexer into local Pygments module (syntax highlighting). The styling is made with Hacks.css in the _static folder
   sys.path.insert(0, os.path.abspath("./includes/AIMMSLexer/Lexer"))
   from aimms import AIMMSLexer
   from pygments.formatters import HtmlFormatter
   sphinx.add_lexer("aimms", AIMMSLexer())

   # for copy code snippet, css file also referred to in html_context
   sphinx.add_stylesheet('copycode.css')
   sphinx.add_javascript('copycode.js')
   sphinx.add_javascript("https://cdn.jsdelivr.net/npm/clipboard@1/dist/clipboard.min.js")

   #To handle redirections
   handle_redirections = False
   if handle_redirections or os.name != 'nt':
		sphinx.add_config_value('redirects_file', 'redirects', 'env')
		sphinx.connect('builder-inited', generate_redirects)   
 
highlight_language = 'aimms'