# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import time
import unicodedata
import MySQLdb.cursors
from scrapy import log
from scrapy.conf import settings
from subprocess import Popen, PIPE
from twisted.enterprise import adbapi

class DeliciousPipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLStorePipeline(object):

    def __init__(self):
        # @@@ hardcoded db settings
        # TODO: make settings configurable through settings
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            db          = settings['DATABASE_NAME'],
            user        = settings['DATABASE_USER'],
            passwd      = settings['DATABASE_PASSWORD'],
            cursorclass = MySQLdb.cursors.DictCursor,
            charset     = 'utf8',
            use_unicode = True
        )

    def process_item(self, item, spider):
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._insert, item)
        query.addErrback(self.handle_error)

        return item

    def _insert(self, tx, item):
        tx.execute("INSERT IGNORE INTO `" + settings['TABLE_NAME'] + "`\
                        (title, link, username, bookmarks, tags, date, hash)\
                    VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (item['title'],
             item['link'],
             item['username'],
             item['bookmarks'],
             item['tags'],
             item['date'],
             item['hash'])
        )

    def handle_error(self, e):
        log.err(e)