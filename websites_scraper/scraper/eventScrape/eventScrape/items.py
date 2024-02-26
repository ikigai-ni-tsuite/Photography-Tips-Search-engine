# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EventscrapeItem(scrapy.Item):
    title = scrapy.Field(default=None)
    link = scrapy.Field(default=None)
    tags = scrapy.Field(default=None)
    date = scrapy.Field(default=None)
    place = scrapy.Field(default=None)
    