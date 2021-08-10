rm -rf naver_movie
scrapy startproject naver_movie

cd naver_movie/naver_movie/spiders
scrapy genspider NaverMovie movie.naver.com/movie/running/current.naver
cd ../../../
