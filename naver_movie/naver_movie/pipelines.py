import datetime
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class NaverMoviePipeline:

    def __init__(self):
        pass

    def open_spider(self, spider):
        spider.logger.info("Pipeline Started.")


    def process_item(self, item, spider):

        if item.get("rate") != "0":
            item["is_pass"] = True
            item["crawled_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            return item
        else:
            raise DropItem(f'Dropped Item. This Rate is {item.get("rate")}')



    def close_spider(self, spider):
        spider.logger.info("Pipeline Closed.")
