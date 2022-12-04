# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderSteamItem(scrapy.Item):
    name = scrapy.Field()
    categories = scrapy.Field()
    reviews_number = scrapy.Field()
    overall_score = scrapy.Field()
    release_date = scrapy.Field()
    developer = scrapy.Field()
    tags = scrapy.Field()
    price = scrapy.Field()
    available_platforms = scrapy.Field()
