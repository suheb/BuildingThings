#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Suhaib Khan'
SITENAME = 'Building things'
SITEURL = 'http://suheb.in'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
MENUITEMS = (('Home', '/'),
         ('Resume', 'http://suheb.in/resume'),)

# Social widget
SOCIAL = (('linkedin', 'https://linkedin.com/in/suhebk'),
          ('github', 'https://github.com/suheb'),
          ('facebook', 'https://www.facebook.com/suhebjerk'),
          ('twitter', 'https://twitter.com/iamsuheb'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme'

STATIC_PATHS = ['assets', 'CNAME']

USE_LESS = True

AUTHORS_BIO = {
  "suheb": {
    "name": "Suhaib Khan",
    "cover": "assets/images/avatar.png",
    "image": "assets/images/avatar.png",
    "website": "http://suheb.in",
    "location": "New Delhi",
    "bio": "A software developer passionate about building things!"
  }
}
