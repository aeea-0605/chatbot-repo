import datetime
import MySQLdb
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from naver_movie.config import db_info


class NaverMoviePipeline:

    def __init__(self):
        self.conn = MySQLdb.connect(**db_info)
        self.curs = self.conn.cursor()

    def open_spider(self, spider):
        spider.logger.info("Pipeline Started.")
        QUERY = """
CREATE TABLE IF NOT EXISTS naver_movie (
id INT PRIMARY KEY AUTO_INCREMENT, 
title TEXT, 
link TEXT,
rate FLOAT,
genre TEXT, 
score FLOAT,
view FLOAT,
director TEXT,
actor TEXT,
crawled_time TEXT);
"""
        self.curs.execute(QUERY.replace("\n", ""))


    def process_item(self, item, spider):

        if item.get("rate") != "0":
            # item["is_pass"] = True
            item["crawled_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.curs.execute(f'INSERT INTO naver_movie (title, link, rate, genre, score, view, director, actor, crawled_time) VALUES ("{item.get("title")}", "{item.get("link")}", {item.get("rate")}, "{item.get("genre")}", {item.get("score")}, {item.get("view")}, "{item.get("director")}", "{item.get("actor")}", "{item.get("crawled_time")}");')

            spider.logger.info("Item to DB inserted.")
            return item
        else:
            raise DropItem(f'Dropped Item. This Rate is {item.get("rate")}')



    def close_spider(self, spider):
        spider.logger.info("Pipeline Closed.")

        self.conn.commit()
        self.conn.close()