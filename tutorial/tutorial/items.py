# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoneyItem(scrapy.Item):
    title    = scrapy.Field()
    content  = scrapy.Field()
    category = scrapy.Field()
    url      = scrapy.Field()
    dt       = scrapy.Field()

