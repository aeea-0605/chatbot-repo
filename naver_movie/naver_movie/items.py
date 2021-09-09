import scrapy


class NaverMovieItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    rate = scrapy.Field()
    genre = scrapy.Field()
    score = scrapy.Field()
    view = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    # is_pass = scrapy.Field()
    crawled_time = scrapy.Field()
