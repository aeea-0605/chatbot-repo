import scrapy
import re
from ..items import NaverMovieItem


class NaverMovieSpider(scrapy.Spider):
    name = 'NaverMovie'
    allowed_domains = ['movie.naver.com']
    start_urls = ['http://movie.naver.com/movie/running/current.naver']

    def parse(self, response):
        
        for element in response.css('ul.lst_detail_t1 > li'):
            link = response.urljoin(element.css('dl > dt.tit a::attr(href)').get(default=None))
            rate = element.xpath('./dl/dd[1]/dl[2]/dd/div/span[1]/text()').get("0")

            yield scrapy.Request(link, callback=self.content_parse, meta={"rate": rate})


    def content_parse(self, response):
        title = response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[1]/text()').extract_first()
        genre = response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]/a/text()').get()
        s_list = response.xpath('//*[@id="actualPointPersentBasic"]/div/em/text()').extract()
        score = ''.join(s_list)
        try:
            view = response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[5]/div/p/text()').extract()[0]
            view = "".join(re.findall("[\d]", view))
        except:
            view = ""
        director = response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a/text()').get()
        a_list = response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[3]/p/a/text()').extract()
        actor = ','.join(a_list)

        yield NaverMovieItem(title=title, link=response.url, rate=response.meta["rate"], genre=genre, score=score, view=view, director=director, actor=actor)