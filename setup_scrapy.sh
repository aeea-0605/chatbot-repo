# Scrapy project 폴더 생성
rm -rf naver_movie
scrapy startproject naver_movie

# spider.py 생성
cd naver_movie
scrapy genspider NaverMovie movie.naver.com/movie/running/current.naver
