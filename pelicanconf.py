#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


# Author and site.
AUTHOR = 'vfhky'
SITENAME = 'TypeCodes'
SITESUBTITLE = 'Beauty of programming'
SITEURL = 'https://typecodes.com'
SITEURL_CDN = 'https://cdn.typecodes.com'
SITEURL_CDN_CSS = 'https://cdn.typecodes.com/libs/css/pelican_vfhky_paraiso-light.min.css'
TIMEZONE = 'Asia/Shanghai'


DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M"
DEFAULT_LANG = u'zh'
# Delete the output directory, and all of its contents, before generating new files. This can be useful in preventing older, unnecessary files from persisting in your output. However, this is a destructive setting and should be handled with extreme care.
DELETE_OUTPUT_DIRECTORY = True


# When creating a short summary of an article, this will be the default length (measured in words) of the text created. This only applies if your content does not otherwise specify a summary. Setting to None will cause the summary to be a copy of the original content.
SUMMARY_MAX_LENGTH = 20



# 底部栏git相关
COMMIT_ID = ''
COMMIT_ICON = 'https://cdn.typecodes.com/libs/img/git.png'
COMMIT_DATE = ''
# 底部栏构建相关
BUILD_ID = ''
BUILD_CUR_ID = ''
BUILD_DATE = ''




#  Theme and plugins
#  Theme requires http://github.com/duilio/pelican-octopress-theme/
#  Plugins require http://github.com/getpelican/pelican-plugins/
# THEME = "tuxlite_tbs"
#THEME = "zurb-F5-basic"
#THEME = "pelican-themes/blue-penguin"
#THEME = "pelican-themes/pelican-octopress"
THEME = "pelican-themes/pelican-typecho"
PLUGIN_PATHS = [u"pelican-plugins"]
PLUGINS = [
	u"sitemap",
    u"minchin.pelican.plugins.summary",
	#u"summary", 
	#u"gzip_cache",
]

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}


# Single pages on header block.
VFHKY_HEAD_PAGE_MAP = [ 
     #("Contributors", "contributors.html"),
     ("Archives", "archives.html"),
     ("About", "about.html"),
]


# Disqus comments.
DISQUS_SITENAME = u"typecodes"
# Your GitHub URL (if you have one). It will then use this information to create a GitHub ribbon.
#GITHUB_URL = u"https://github.com/vfhky/vfhky.github.io"


# Path to content directory to be processed by Pelican. 
PATH = 'content'
# A list of directories and files to look at for pages, relative to PATH.
PAGE_PATHS = ['pages']
# A list of directories and files to look at for articles, relative to PATH.
ARTICLE_PATHS = ['articles']
# A list of directories to exclude when looking for articles in addition to PAGE_PATHS.
ARTICLE_EXCLUDES = []

# static paths will be copied without parsing their contents
STATIC_PATHS = [u"static/",
                "extra/40x.html",
                'extra/50x.html',
                "extra/robots.txt",
                'extra/favicon.ico',
                "extra/verification.xml",
                "extra/BingSiteAuth.xml",
                "extra/google583eda29dcbe6a0c.html",
                ]
# path-specific metadata
EXTRA_PATH_METADATA = {
    "extra/40x.html": {"path": "40x.html"},
    'extra/50x.html': {'path': '50x.html'},
    "extra/robots.txt": {"path": "robots.txt"},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    "static/verification.xml": {"path": "verification.xml"},
    "static/BingSiteAuth.xml": {"path": "BingSiteAuth.xml"},
    "extra/google583eda29dcbe6a0c.html": {"path": "google583eda29dcbe6a0c.html"},
}


# Blogroll
# LINKS = (('diaosbook', 'http://diaosbook.com/'),
#         )
# Use self-defined variable to links otherthan Blogroll
VFHKY_LINKS_1 = {
}
VFHKY_LINKS_2 = {
}
VFHKY_LINKS_3 = {
}


# If you want to generate custom pages besides your blog entries, you can point any Jinja2 template file with a path pointing to the file and the destination path for the generated file.     
TEMPLATE_PAGES = {
	'about.html': 'about.html',
	#'contributors.html': 'contributors.html',
	'links.html': 'links.html',
	'search.html': 'search.html',
}


# Social widget
SOCIAL = (
		  ('Github', 	'https://github.com/vfhky'),
          ('SAE', 		'http://vfhky.sinaapp.com/'),
          ('Weibo', 	'http://weibo.com/typecodes'),
         )


# RSS/Atom feeds
FEED_ATOM = 'atom.xml'
FEED_RSS = 'feed.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# add a nice section on the sidebar with a list of GitHub repositories of the user.
# GITHUB_USER = 'vfhky'
# GITHUB_REPO_COUNT = 5
# GITHUB_SKIP_FORK = False
# GITHUB_SHOW_USER_LINK = False

# sharing via Twitter, Google Plus, and Facebook.
# TWITTER_USER = 'vfhky'
# GOOGLE_PLUS_ID = 101192347122765496150
# FACEBOOK_LIKE = True

# Extra Twitter options (default values are shown):
# TWITTER_WIDGET_ID: (required to enable feed) ID obtained from twitter settings
# TWITTER_TWEET_BUTTON: False show twitter tweet button
# TWITTER_FOLLOW_BUTTON: False show twitter follow button
# TWITTER_TWEET_COUNT: 3 number of latest tweets to show
# TWITTER_SHOW_REPLIES: 'false' whether to list replies among latest tweets
# TWITTER_SHOW_FOLLOWER_COUNT: 'true' show number of followers

# Extra google plus options (default values are shown):
# GOOGLE_PLUS_ONE: False show +1 button
# GOOGLE_PLUS_HIDDEN: False hide the google plus sidebar link.

# Google Analytics
# GOOGLE_ANALYTICS: "UA-XXXX-YYYY" to activate Google Analytics(classic)
# GOOGLE_UNIVERSAL_ANALYTICS: "UA-XXXX-Y" to activate Google Universal Analytics
# GOOGLE_UNIVERSAL_ANALYTICS_COOKIEDOMAIN: 'auto' optional cookie domain setting for Google Universal Analytics
# GOOGLE_ANALYTICS_DISPLAY_FEATURES: True to enable Display Advertiser Features. This setting works for both Classic Analytics and Universal Analytics.


# Sidebar image.
# SIDEBAR_IMAGE: Adds specified image to sidebar. Example value: "images/author_photo.jpg"
# SIDEBAR_IMAGE_ALT: Alternative text for sidebar image
# SIDEBAR_IMAGE_WIDTH: Width of sidebar image
# SEARCH_BOX: set to true to enable site search box
SEARCH_BOX = True
# SITESEARCH: [default: 'http://google.com/search'] search engine to which search form should be pointed (optional)


# set to true to enable the qr code generation for articles and pages by browser.
# QR_CODE = True


# FeedBurner integration.
# FEED_FEEDBURNER: set this to the part of your FeedBurner URL after the http://feeds.feedburner.com/ to set the displayed feed URL to your FeedBurner URL. This also disables generation of the RSS and ATOM tags, regardless of whether you've set the FEED_RSS or FEED_ATOM variables. This way, you can arbitrarily set your generated feed URL while presenting your FeedBurner URL to your users.


# Isso self-hosted comments
# Isso is intended to be a Free replacement for systems like Disqus. Because it is self-hosted, it gives you full control over the comments posted to your website.
# ISSO_SITEURL: (required to enable) set this to the URL of the server Isso is being served from without a trailing slash. Example: http://example.com


# X min read
# medium.com like "X min read" feature. You need to activate the plugin post_stats for this to work (default values are shown):
X_MIN_READ = False


# set to path of your favicon. The default is empty in which case the template will use the hardcoded address favicon.png.
# FAVICON_FILENAME = ''

# Main Navigation (menu bar)：主菜单
# Whether to display pages on the menu of the template. Templates may or may not honor this setting.
DISPLAY_PAGES_ON_MENU = False
# show categories
DISPLAY_CATEGORIES_ON_MENU = True
# show feed icons (on the very right side)
DISPLAY_FEEDS_ON_MENU = False
# MENUITEMS: () show static links (before categories)
# MENUITEMS_MIDDLE: () show static links (between pages and categories) e.g.: MENUITEMS_MIDDLE = ( ('link1', '/static/file1.zip'), )
# MENUITEMS_AFTER: () show static links (after categories) e.g.: MENUITEMS_AFTER = ( ('link2', '/static/file2.pdf'), )


# Markup for Social Sharing:
# In order to specify page title, description, image and other metadata for customized social sharing (e.g. Twitter cards), you can add the following metadata to each post:
# title: The title of the post. This is expected for any post.
# description: A long form description of the post.
# social_image: A path to an image, relative to SITEURL. This image will show up next to the other information in social shares.
# twitter_site: A Twitter handle, e.g. @getpelican for the owner of the site.
# twitter_creator: A Twitter handle, e.g. @getpelican for the author of the post.
# In addition, you can provide a default post image (instead of setting social_image in the post metadata), by setting SOCIAL_IMAGE in your pelicanconf.
# These can be used for social sharing on Google+, Twitter, and Facebook as well as provide more detailed page data for Google Search. In order to enable in each respective channel, your post metadata needs to specify:
# title: The title of the post. This is expected for any post.
# use_schema_org: true: For Google and Google+ specific meta tags.
# use_open_graph: true: For Facebook specific meta tags.
# use_twitter_card: true: For Twitter specific meta tags.


# The maximum number of articles to include on a page, not including orphans. False to disable pagination.
DEFAULT_PAGINATION = 8

# configure where subsequent pages are created.
# PAGINATION_PATTERNS = (
  #   (1, '/', '{base_name}/index{number}.html'),
    # (2, '{base_name}/', '{base_name}/index{number}.html'),
# )

PAGINATION_PATTERNS = (
    	(1, '/', '{name}.html'),
    	(2, '{base_name}/', '{name}{number}.html'),
	)


# Translations
# DEFAULT_LANG = 'en'	The default language to use.
# TRANSLATION_FEED_ATOM = 'feeds/all-%s.atom.xml' [3]	Where to put the Atom feed for translations.
# TRANSLATION_FEED_RSS = None, i.e. no RSS	Where to put the RSS feed for translations.



# The default category to fall back on.
DEFAULT_CATEGORY = u'cseries'


# URL settings.
ARCHIVES_URL 		= 	'archives'
ARTICLE_URL 		= 	'{category}/{slug}.html'
ARTICLE_SAVE_AS 	= 	ARTICLE_URL

PAGE_URL 			= 	'{slug}.html'
PAGE_SAVE_AS 		= 	PAGE_URL
PAGE_LANG_SAVE_AS 	= 	False

TAG_URL 			= 	'tag/{slug}.html'
TAG_SAVE_AS 		= 	TAG_URL
TAGS_URL 			= 	False
TAGS_SAVE_AS 		= 	False

CATEGORY_URL 		= 	'{slug}/index.html'
CATEGORY_SAVE_AS 	= 	CATEGORY_URL

AUTHOR_SAVE_AS 		= 	False
AUTHORS_SAVE_AS 	= 	False


# Defines whether Pelican should use document-relative URLs or not. Only set this to True when developing/testing and only if you fully understand the effect it can have on links/feeds.
# can be useful in development, but set to False when you're ready to publish.
RELATIVE_URLS = False

#MARKDOWN = {
#    'extension_configs': {
#        'markdown.extensions.codehilite': {'css_class': 'tphighlight'},
#        'markdown.extensions.extra': {},
#        'markdown.extensions.meta': {},
#    },
#    'output_format': 'html5',
#}

