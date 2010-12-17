import string
import re

from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Join
from scrapy.utils.markup import remove_entities

from delicious.items import Bookmark, BookmarkLoader

class DeliciousSpider(BaseSpider):
    name = "delicious.com"
    allowed_domains = ["delicious.com", "www.delicious.com"]
    start_urls = [
        "http://www.delicious.com/tag/delicious",
    ]

    rules = (
        # Extract links from all pages and parse them with the regular method
        Rule(SgmlLinkExtractor(allow=('.', )), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        items = []
        date = None
        for bookmark in HtmlXPathSelector(response).select('//div[contains(@class, "bookmark")]'):
            loader = BookmarkLoader(Bookmark(), bookmark)
            link = bookmark.select('.//div[contains(@class, "data")]/h4/a/@href').extract()

            loader.add_xpath('title',       './/div[contains(@class, "data")]/h4/a/text()')
            loader.add_value('link',        link)
            loader.add_value('hash',        link)
            loader.add_xpath('bookmarks',   './/div[contains(@class, "data")]/div/div/a/span/text()')
            loader.add_xpath('username',    './/div[contains(@class, "meta")]//a[1]/@href')
            loader.add_xpath('tags',        './/div[contains(@class, "meta")]/div[contains(@class, "tagdisplay")]/child::ul/li/a/text()')

            # Hack for iterations where dates are not available in the current bookmark
            if bookmark.select('.//div[contains(@class, "dateGroup")]/@title').extract():
                date = bookmark.select('.//div[contains(@class, "dateGroup")]/@title').extract()
            loader.add_value('date', date)

            items.append(loader.load_item())

        return items