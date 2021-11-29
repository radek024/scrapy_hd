# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def remove_text(value):
    args = ['szac.', 'zł', 'wyświetleń', '\n', '\t']
    for arg in args:
        if(value.find(arg)>0):
            value = value.replace(arg,'').strip()
    return value

def remove_notSell(value):
    return value.replace('—','0').strip()    

def removeStart_notSell(value):
    return value.replace('start','').strip()    



class WcnauctionsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    category = scrapy.Field(input_processor = MapCompose(remove_tags, remove_text), output_processor = TakeFirst())
    condition =scrapy.Field(input_processor = MapCompose(remove_tags, remove_text), output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags,remove_text, remove_notSell), output_processor = TakeFirst())
    est_price = scrapy.Field(input_processor = MapCompose(remove_text,removeStart_notSell, remove_tags), output_processor = TakeFirst())
    bids = scrapy.Field(input_processor = MapCompose(remove_tags, remove_text), output_processor = TakeFirst())
    views = scrapy.Field(input_processor = MapCompose(remove_tags, remove_text), output_processor = TakeFirst())
    photoUrl = scrapy.Field()
    link = scrapy.Field()
    pass
