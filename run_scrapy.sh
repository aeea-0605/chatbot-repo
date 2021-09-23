# scrapy.cfg 가 있는 디렉토리로 이동
cd /home/ubuntu/notebooks/chatbot-repo/naver_movie

# result.csv가 있으면 제거하고 scrapying 시작
rm result.csv
scrapy crawl NaverMovie -o result.csv
