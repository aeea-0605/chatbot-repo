BOT_NAME = 'naver_movie'

SPIDER_MODULES = ['naver_movie.spiders']
NEWSPIDER_MODULE = 'naver_movie.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 2

COOKIES_ENABLED = True

DEFAULT_REQUEST_HEADERS = {
  "Referer": "https://movie.naver.com/"
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
}

RETRY_ENABLED = True
RETRY_TIMES = 2

ITEM_PIPELINES = {
   'naver_movie.pipelines.NaverMoviePipeline': 300,
}
