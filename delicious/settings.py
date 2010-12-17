# Scrapy settings for delicious project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
# 
#     scrapy/conf/default_settings.py
#

BOT_NAME            = 'delicious'
BOT_VERSION         = '1.0'

SPIDER_MODULES      = ['delicious.spiders']
NEWSPIDER_MODULE    = 'delicious.spiders'
DEFAULT_ITEM_CLASS  = 'delicious.items.DeliciousItem'
USER_AGENT          = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES      = ['delicious.pipelines.DeliciousPipeline']

DOWNLOAD_DELAY      = 0.25 # random interval between 0.5 and 1.5 * DOWNLOAD_DELAY

# Database connection information
DATABASE_NAME       = 'delicious'
DATABASE_USER       = 'root'
DATABASE_PASSWORD   = 'password'
TABLE_NAME          = 'bookmarks'