BOT_NAME = 'naver_movie'

SPIDER_MODULES = ['naver_movie.spiders']
NEWSPIDER_MODULE = 'naver_movie.spiders'

ROBOTSTXT_OBEY = False


DOWNLOAD_DELAY = 2

COOKIES_ENABLED = True

DEFAULT_REQUEST_HEADERS = {
  "Referer": "https://movie.naver.com/"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'naver_movie.middlewares.NaverMovieSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
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



# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
