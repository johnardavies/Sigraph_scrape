import scrapy


class SigraphScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    text = scrapy.Field()
    title = scrapy.Field()
    pass
