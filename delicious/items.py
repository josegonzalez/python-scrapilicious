# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html
import string

from scrapy.item import Item, Field
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Join
from scrapy.utils.markup import remove_entities
from delicious.processors import HashStringList, ParseDate, ParseUsername

class DeliciousItem(Item):
    pass

class Bookmark(Item):
    title       = Field()
    link        = Field()
    date        = Field()
    username    = Field()
    hash        = Field()
    bookmarks   = Field(default=0)
    tags        = Field(default=None)
    pass


class BookmarkLoader(XPathItemLoader):
    default_input_processor = MapCompose(remove_entities, string.strip)
    default_output_processor= TakeFirst()

    username_out= ParseUsername()
    date_out    = ParseDate()
    hash_out    = HashStringList()
    tags_out    = Join(separator=" ")
