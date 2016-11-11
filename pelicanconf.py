#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jose Teneb'
SITENAME = u"Jose' log"
SITESUBTITLE = u'Patagonico, Desarrollador de cosas, ahora medio instalado en Dublin'
SITEDESCRIPTION = u'' 
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Dublin'
DEFAULT_LANG = u'es'
DEFAULT_DATE_FORMAT = '%d %b, %Y'

PATH = 'content'
THEME = 'themes/strata'
STATIC_PATHS = ['images', 'extra/CNAME', 'extra/robots.txt']

#JINJA_EXTENSIONS = ['jinja2.ext.i18n']

DELETE_OUTPUT_DIRECTORY = True

FAVICON = SITEURL + '/images/favicon.ico'
ROBOTS = 'index, follow'
DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['pelican-plugins', 'plugins']
#PLUGIN_PATHS = ['../pelican-plugins']
#PLUGINS = ['i18n_subsites', 'sitemap', 'pelican_gist']
PLUGINS = ['i18n_subsites', 'sitemap', 'pelican-gist']

#PAGE_URL = '{slug}/'
#PAGE_SAVE_AS = '{slug}/index.html'
#LOCALE = 'es_ES'

I18N_SUBSITES = {
        'en': { 
            'SITENAME': "Jose' log",
            'OUTPUT_PATH': 'output/en/',
            'SITESUBTITLE' : u'From Patagonia, Developer of things, now living in Dublin',
            'INDEX_SAVE_AS': 'index.html',
            'I18N_UNTRANSLATED_PAGES': 'hide',
            'I18N_UNTRANSLATED_ARTICLES': 'hide',
 #           'LOCALE': "en_EN",            #This is somewhat redundant with DATE_FORMATS, but IMHO more convenient
			'MENUITEMS' : (('Blog', 'archives.html'), 
						 #('Projects', 'pages/projects.html'),
						 ('About', 'pages/about.html'),			 
						)
            },
        } 

languages_lookup = {
			'en': 'English',
			'es': 'Español',
		}

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]


JINJA_FILTERS = {
    'lookup_lang_name': lookup_lang_name
    }

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


LINKS = ()

MENUITEMS = (('Blog', 'archives.html'), 
			 ('Proyectos', 'pages/projects.html'),
			 ('Sobre el autor', 'pages/about.html'),			 
			)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/firedix'),
          ('linkedin', 'http://www.linkedin.com/in/joseteneb'),
          ('github', 'http://github.com/joseteneb'),)

EMAIL = "contact@joseteneb.com"

EXTRA_PATH_METADATA = {
	'extra/CNAME': {'path': 'CNAME'},
	'extra/robots.txt': {'path': 'robots.txt'},
}

GOOGLE_ANALYTICS = "UA-72073843-1"

PROFILE_IMAGE = "profile.jpg"
DISQUS_SITENAME = 'joseteneb'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
