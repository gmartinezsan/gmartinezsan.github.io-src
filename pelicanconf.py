#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


# General information of the site
AUTHOR = 'Gabriela Martinez'
SITENAME = 'Avoiding code'
SITEURL = ''
SITE_DESCRIPTION = 'From software development to cloud deployment, and everything in between'
PATH = 'content'
TIMEZONE = 'America/Mexico_City'
DEFAULT_LANG = 'En'


#Paths for articles and pages
ARTICLE_PATHS = ['posts',]
ARTICLE_URL = '{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
STATIC_PATHS = ['images', 'extra']

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'theme/css/custom.css'}
}


# Theme configuration
THEME = 'theme'
PLUGIN_PATHS = ['plugins/', ]
PLUGINS = ['i18n_subsites', ]

BANNER = 'images/alejandro-escamilla-unsplash.jpg'
BANNER_SUBTITLE = "time : {'always', 'learning'}"
BANNER_ALL_PAGES = True
CUSTOM_CSS = 'theme/css/custom.css'

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

BOOTSTRAP_NAVBAR_INVERSE = True
BOOTSTRAP_THEME = 'readable'
PYGMENTS_STYLE = 'monokai'
FAVICON = 'images/favicon.png'
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 3


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget

SOCIAL = (('Twitter', 'https://twitter.com/gabrymartinez'),
          ('Github', 'https://github.com/gmartinezsan'),
	  ('Medium', 'https://medium.com/@gabrymartinez'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

OUTPUT_PATH = 'output'




