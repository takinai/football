import scrapy

class Table(scrapy.Item):
    team = scrapy.Field()
    key = scrapy.Field()
    value = scrapy.Field()
