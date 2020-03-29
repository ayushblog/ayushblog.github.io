#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ayush Kumar Shah'
SITENAME = 'Ayush Kumar Shah'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Kathmandu'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/Flex'

PLUGIN_PATHS = ['./pelican-plugins']

### Flex configurations

PLUGINS = ['sitemap', 'post_stats', 'feed_summary']
SITEURL = 'http://localhost:8000'
SITETITLE = 'Ayush Kumar Shah'  # Replace with your name
SITESUBTITLE = 'Ideas and Thoughts'
SITELOGO = '/images/profile.png'
FAVICON = '/images/favicon.ico'

# Sitemap Settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# Add a link to your social media accounts
SOCIAL = (
    ('github', 'https://github.com/ayushkumarshah'),
    ('envelope', 'mailto:ayushkumarshah@gmail.com'),
    ('linkedin','https://np.linkedin.com/in/ayush7'),
    ('twitter','https://twitter.com/ayushkumarshah7'),
    ('facebook','https://www.facebook.com/ayushkumarshah'),
    ('reddit','https://www.reddit.com/user/ayushkumarshah')
)

STATIC_PATHS = ['images', 'extra']

# # Blogroll

# Main Menu Items
MAIN_MENU = True
MENUITEMS = (('Archives', '/archives'),('Categories', '/categories'),('Tags', '/tags'))

# Code highlighting theme
PYGMENTS_STYLE = 'friendly'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'