import scrapy


class NavermovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.naver.com']
    start_urls = ['http://movie.naver.com/movie/running/current.naver']

    def parse(self, response):
        pass
