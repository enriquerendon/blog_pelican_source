#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Enrique Rendon'
SITENAME = "Enrique's Blog"
SITEURL = ''

PATH = 'content'

ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_PATHS = ['pages']
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'



STATIC_PATHS = ['images', 'docs']
OUTPUT_PATH = '../output'

THEME = '../../pelican-themes/pelican-bootstrap3'
PLUGIN_PATHS = ['../../pelican-plugins/', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n'],}
BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = 'monokai'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('iTrendOn', 'http://itrendon.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/iTrendOn'),
          ('GitHub', 'https://github.com/prognostech'),
          ('GitLab', 'https://gitlab.com/enrique.rendon'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
