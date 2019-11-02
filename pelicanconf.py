#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'wenning'
SITENAME = "wenning's blog"
# SITEURL = 'https://htwenning.github.io'
SITEURL = ''  # use relative path
THEME = 'mytheme'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = [".git"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = 'feeds/all.rss.xml'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


PLUGIN_PATHS = ["plugins"]
PLUGINS = ['standalone_categories',]

STANDALONE_CATEGORY_PAGES = [
    {
        'category_name': 'Travels',
        'page_template': 'timeline',
        'article_template': 'article'
    },
]
