#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
###############################################################
###############################################################   Site abt.
###############################################################
AUTHOR = u'MoMoKo'
SITENAME = u'MoMoKo.in'
SITESUBTITLE = u'丸子家.在内'
SITEURL = 'http://MOMOKO.in'
DISQUS_SITENAME = u"momokoin" #填入你的Shortname

MARKUP = ('md', )#'rst', 'html', 
#   TIMEZONE = 'Europe/Paris'
TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
        'zh_CN': '%Y-%m-%d %H:%M',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'
DEFAULT_DATE = 'fs' # use filesystem's mtime

#LOCALE = ('zh_CN.utf8',)
DEFAULT_LANG = u'zh_CN'
FILENAME_METADATA = '(?P<slug>.*)'

###############################################################
###############################################################   Plugins abt.
###############################################################
# Plugins 
PLUGINS=['_plugins.sitemap'
    , '_plugins.extract_toc'
    #, '_plugins.gzip_cache'
    #, u"pelican.plugins.disqus_static"
    ]
    
#   upgraded Pelican 3.3 must self open them
MD_EXTENSIONS = (['codehilite(css_class=highlight)'
    , 'extra', 'abbr', 'attr_list', 'def_list', 'fenced_code', 'smart_strong'
    , 'admonition', 'meta', 'tables', 'sane_lists'
    , 'toc'
    ])


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
###############################################################
###############################################################   Template abt.
###############################################################
THEME = "_themes/fresh"
BOOTSTRAP_THEME = 'readable'

DEFAULT_PAGINATION = 1
TAG_CLOUD_MAX_ITEMS = 10

DISPLAY_CATEGORIES_ON_MENU = None      # 分类标签是否显示在导航
# Social widget
ADDTHIS_PROFILE = True

#GITHUB_USER = "ZoomQuiet"
#MENUITEMS = ( ('Archives', SITEURL + '/archives.html')
#        , ('PyConChina', 'http://cn.pycon.org')
#        ,('News', 'http://news.pychina.org')
#        )

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS= None
SOCIAL = (('GitHub', 'https://github.com/PyConChina')
        , ('Weekly', 'http://weekly.pychina.org')
        , ('News', 'http://news.pychina.org')
        , ('rss', SITEURL + '/' + FEED_ALL_ATOM)
        , ('Archives', SITEURL + '/archives.html')
        , ('CPyUG', 'https://gitcafe.com/CPyUG')
        , ('Wiki', 'http://wiki.woodpecker.org.cn/moin/CPUG')
        , ('weibo', 'http://weibo.com/pyconcn')
        , ('O.B.P', 'http://weibo.com/openbookproject')
        )
# Blogroll
LINKS =  None
###############################################################
###############################################################   Publish abt.
###############################################################
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = None  #!!! for .github.io can not clean outupt/.git
DEFAULT_CATEGORY = u'Chaos'

TEMPLATE_PAGES = {
        "404.html": "404.html",
        }

STATIC_PATHS = ['_images', '_files'
    , '_extra/.nojekyll'
    , '_extra/robots.txt'
    , '_extra/favicon.ico'
    , '_extra/README.md'
    , '_extra/CNAME'
    , '_extra/LICENSE'
    #, '_extra/storyjs-embed.js'
    #, '_extra/timeline-min_2.17.js'
    #, '_extra/zh-ch_2.17.js'
    , '_extra/sanchuan_news.json'
    , '_extra/sanchuan_storyjs-embed.js'
    , '_extra/sanchuan_timeline-min.js'
    , '_extra/sanchuan_timeline.css'
    , '_extra/sanchuan_zh-ch.js'
    , '_extra/loading.gif'
    , '_extra/timeline.png'
    #, '_extra/basic.json'
    , '_extra/spreadsheet_momoko.json'

    ]

EXTRA_PATH_METADATA = {'_extra/robots.txt': {'path': 'robots.txt'}
    , '_extra/favicon.ico': {'path': 'favicon.ico'}
    , '_extra/README.md': {'path': 'README.md'}
    , '_extra/CNAME': {'path': 'CNAME'}
    , '_extra/LICENSE': {'path': 'LICENSE'}
    #, '_extra/basic.json': {'path': 'family/0AgPxePCteZKodE82R2NCdzZjcWNZcy1VYk9aYWgzcUE'}
    #, '_extra/spreadsheet_momoko.json': {'path': 'spreadsheet_momoko.json'}
    , '_extra/spreadsheet_momoko.json': {'path': 'family/0AgPxePCteZKodE82R2NCdzZjcWNZcy1VYk9aYWgzcUE'}
    #, '_extra/sanchuan_news.json': {'path': 'family/0AgPxePCteZKodE82R2NCdzZjcWNZcy1VYk9aYWgzcUE'}
    , '_extra/sanchuan_storyjs-embed.js': {'path': 'sanchuan_storyjs-embed.js'}
    , '_extra/sanchuan_timeline-min.js': {'path': 'sanchuan_timeline-min.js'}
    , '_extra/sanchuan_timeline.css': {'path': 'sanchuan_timeline.css'}
    , '_extra/sanchuan_zh-ch.js': {'path': 'sanchuan_zh-ch.js'}
    , '_extra/loading.gif': {'path': 'loading.gif'}
    , '_extra/timeline.png': {'path': 'timeline.png'}
    }

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'






