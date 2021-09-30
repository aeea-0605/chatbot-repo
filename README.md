# 자동화 데이터 파이프라인 및 챗봇 서비스 프로젝트
---

## 1. 개요
<br/>

### **1-1. 프로젝트 목적**
네이버 <상영작·예정작> 카테고리의 영화 정보에 대한 자동화된 데이터 파이프라인 구축 및 OpenAPI를 사용한 다양한 기능(영화, 날씨, 번역)의 Slack 챗봇 서비스를 제공하는 프로젝트입니다.

<br/>

### **1-2. 프로젝트 목표**
- Slack의 워크스페이스에서 Client와 Request & Response 하여 동적인 컨텐츠를 제공하는 챗봇을 구현합니다.
- AWS의 Lambda를 사용하여 크롤링서버를 컨트롤합니다.
- scrapy와 chatbot에 대한 logger를 만들어 history를 기록합니다. (9월 29일 추가)

<br/>

### **1-3. 기술적 Summary**
- Scrapy Framework를 사용한 데이터 ETL
- MySQLdb, sqlalchemy를 사용한 DB 세션 연결 및 DDL, DML
- Lambda & Crontab 을 사용한 자동화 데이터 파이프라인 구축
- Nginx Web Server를 통한 HTTP Server 기능 구현
- Flask Framework를 사용한 Web Application 구축
- Slack의 webhook URL을 통한 챗봇 구현
- OpenAPI를 사용해 챗봇 기능 구현
    - Naver API(papago) : 번역
    - Kakao API(local) : 좌표 반환
    - openweathermap : 날씨
- logging을 사용한 logger 구현

<br/>

### **1-4. 프로젝트 구성도**

```
chatbot-repo
├── chatbot : 챗봇 프로젝트
│   ├── app
│   │   ├── __init__.py : app 생성
│   │   ├── config.py : DB 및 API 정보
│   │   ├── set_logger.py : chatbot logger 설정
│   │   ├── items
│   │   │   └── mysql_movie.py : TABLE 연결
│   │   ├── libs
│   │   │   ├── forecast.py : 날씨 정보 제공
│   │   │   ├── naver.py : 변역 정보 제공
│   │   │   └── slack.py : slack에 메세지 보내는 기능 제공
│   │   └── routes
│   │       └── bot.py : 챗봇의 기능 및 log 기록
│   ├── log
│   │   └── chatbot.log : client가 request에 대한 log 파일
│   └── chatbot.py : flask 실행
├── naver_movie : 영화 크롤링 프로젝트
│   ├── naver_movie
│   │   ├── __init__.py
│   │   ├── config.py : DB 정보
│   │   ├── items.py : 수집할 data에 대한 정보
│   │   ├── middlewares.py
│   │   ├── pipelines.py : 수집 데이터 필터링 및 DB에 저장
│   │   ├── settings.py : scrapy에 대한 설정
│   │   ├── set_logger.py : scrapy logger 설정
│   │   └── spiders
│   │       ├── __init__.py
│   │       └── NaverMovie.py : 크롤링에 대한 코드 및 log 기록
│   ├── log
│   │   └── scrapy.log : scrapy 실행&종료에 대한 log 파일
│   └── scrapy.cfg
├── data.ini : hide variable에 대한 정보
├── run_chatbot.sh : 챗봇 프로젝트 실행 코드
├── run_scrapy.sh : 크롤링 프로젝트 실행 코드
├── setup_chatbot.sh : 챗봇 프로젝트 세팅 코드
└── setup_scrapy.sh : 크롤링 프로젝트 세팅 코드
```

<br/>

---
---
## 2. 결과

### **2-1. 챗봇**

#### **<챗봇 호출>**
<img width="438" alt="스크린샷 2021-09-18 오전 12 21 17" src="https://user-images.githubusercontent.com/80459520/133807895-5c6be44a-667a-4811-8b93-ab791eec7c20.png">

#### **<챗봇 `도움`>**
<img width="541" alt="스크린샷 2021-09-18 오전 12 24 49" src="https://user-images.githubusercontent.com/80459520/133808872-87d7b893-8e84-4a4f-ae3a-d1e2c253d951.png">

#### **<챗봇 `날씨`>**
- 서울에 대한 날씨 정보 요청

<img width="352" alt="스크린샷 2021-09-18 오전 12 26 12" src="https://user-images.githubusercontent.com/80459520/133809745-cd466a3f-c985-4981-9946-89e6b92b1cb7.png">

#### **<챗봇 `영화`>**
- 알고자하는 마지막 순위(숫자) or 전체(문자) 입력
    - 5위까지의 영화 정보 요청

<img width="640" alt="스크린샷 2021-09-18 오전 12 28 07" src="https://user-images.githubusercontent.com/80459520/133811036-6d28b5dc-f0c0-456f-a70c-244c41be6131.png">

- 수집시점에 대한 정보와 5위까지의 영화 정보(제목, 예매율, 평점, 링크) 제공

#### **<없거나 잘못된 명령어 입력>**
<img width="547" alt="스크린샷 2021-09-18 오전 12 32 27" src="https://user-images.githubusercontent.com/80459520/133813613-baf8799e-645e-440f-8106-4442f13de2ed.png">

- 현재 챗봇이 보유한 명령어를 알려주는 정보 제공

<br/>

---
### **2-2 log**

#### **<scrapy log 파일>**
> [scrapy.log](https://github.com/aeea-0605/chatbot-repo/blob/main/naver_movie/log/scrapy.log)
- 크롤링 시작&종료에 대한 로그를 기록해 크롤링 시간 및 수집시기를 알 수 있다.

<br/>

#### **<chatbot log 파일>**
> [chatbot.log](https://github.com/aeea-0605/chatbot-repo/blob/main/chatbot/log/chatbot.log)
- Client가 request한 data에 대한 로그를 기록해 유저가 보낸 명령어 및 원하는 정보를 알 수 있다.
- 로그에 대한 기록을 분석해 해당 챗봇에서 많이 사용되는 명령어를 알 수 있다.

<br/>

#### **< console log during scrapying >**

<img width="400" alt="스크린샷 2021-09-30 오후 3 04 46" src="https://user-images.githubusercontent.com/80459520/135396352-c5274001-8637-4676-8bee-9d5859e41d53.png">

- 최초 파이프라인이 실행될 때, crawled data가 조건을 만족하여 DB에 저장되었을 때, 최후 파이프라인이 종료될 때에 대한 log만 console창에 띄워지도록 설정

<br/>

---
---
## 3. 과정

<br/>

### **3-1. 네이버 영화 크롤링**

#### **1) Scrapy Project 생성**
> [setup_scrapy.sh](https://github.com/aeea-0605/chatbot-repo/blob/main/setup_scrapy.sh)
```
$source setup_scrapy.sh
```
- chatbot-repo 디렉토리에서 실행
    - naver_movie project 폴더 생성 및 수집할 경로에 대한 spider 파일인 `NaverMovie.py` 생성

<br/>

#### **2) naver_movie `items.py` 작성**
> [items.py](https://github.com/aeea-0605/chatbot-repo/blob/main/naver_movie/naver_movie/items.py)
- 수집하고자 하는 영화 정보를 가진 NaverMovieItem class 생성
    -  제목, 링크, 예매율, 장르, 평점, 누적관객수, 감독, 배우, 수집시간에 대한 정보

<br/>

#### **3) naver_movie `NaverMovie.py` 작성**
> [NaverMovie.py](https://github.com/aeea-0605/chatbot-repo/blob/main/naver_movie/naver_movie/spiders/NaverMovie.py)
- `parse`
    1. start url을 받아 영화의 링크와 예매율 데이터 수집 
    2. content_parse에 링크를 yield하며 argument에 예매율을 넣어 함께 보냄
- `content_parse`
    1. response 받은 링크에서 제목, 장르, 평점, 누적관객수, 감독, 배우 데이터 수집
    2. response 받은 url, 예매율 및 수집한 데이터를 NaverMovieItem에 yield item 객체 생성

<br/>

#### **4) DB와 세션 연결을 위한 `config.py` 작성**
> [config.py](https://github.com/aeea-0605/chatbot-repo/blob/main/naver_movie/naver_movie/config.py)
- data.ini의 "db"에 대한 정보를 불러와 db_info 변수에 저장

<br/>

#### **5) naver_movie `pipelines.py` 작성**
> [pipelines.py](https://github.com/aeea-0605/chatbot-repo/blob/main/naver_movie/naver_movie/pipelines.py)
- `__init__` : Mysql DB와 세션 연결 및 Cursor 객체 생성
- `open_spider` : 최초 한 번 log message 출력, naver_movie TABLE에 대한 DDL 쿼리 작성 및 서버에 보냄
- `process_item` : `NaverMovie.py`에서 item 객체를 받아 객체에 대한 필터링 작업 수행
    - 예매가 이루어지지 않은 객체는 Drop
    - 예매가 이루어진 객체에 대해 수집시간 부여 및 naver_movie TABLE에 객체에 대한 정보를 INSERT 후 log message 출력
- `close_spider` : 최후 한 번 log message 출력, 퀴리에 대한 commit 및 세션 종료

<br/>

#### **6) naver_movie `settings.py` 작성**
> [settings.py](https://github.com/aeea-0605/chatbot-repo/blob/main/naver_movie/naver_movie/settings.py)
- robots.txt, MIDDLEWARE, PIPELINES 등에 대한 설정

<br/>

#### **7) Scrapy Project 실행을 위한 `run_scrapy.sh` 작성**
> [run_scrapy.sh](https://github.com/aeea-0605/chatbot-repo/blob/main/run_scrapy.sh)
- -o 옵션을 통해 csv 파일로도 저장

<br/>

#### **8) 자동화를 위한 crontab 파일 작성**
```
PATH=/home/ubuntu/.pyenv/versions/python3/bin:/usr/local/bin
@reboot /bin/bash ~/notebooks/chatbot-repo/run_scrapy.sh
```
- PATH를 통한 경로설정
- `@reboot` 명령어를 통해 서버가 시작될 때 `run_scrapy.sh` 가 실행되어 크롤링을 진행

<br/>

#### **9) AWS lambda의 함수 설정**
- AWS의 인스턴스를 시작시키고 종료시킬 수 있는 두 개의 함수를 작성합니다.
    - 스케쥴 트리거를 기능을 할 Cloud Watch 서비스를 설정
- `start 함수`
    - cron : 00 0 * * ? * (매일 0시 00에 서버 실행)
    - lambda_function.py
    ```
    import json
    import boto3

    def lambda_handler(event, context):
    
        aws_access_key_id = "your aws_access_key_id"
        aws_secret_access_key = "your aws_secret_access_key"
        instance_ids = ["your Instance ID"]
    
        client = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='ap-northeast-2')

        client.start_instances(InstanceIds=instance_ids, DryRun=False)
    
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
    ```
- `stop 함수`
    - cron : 10 0 * * ? * (매일 0시 10분에 서버 종료)
        - 데이터 ETL이 완료된 후 서버 종료
    - lambda_function.py
        - start의 lambda_function.py에서 start_instances method를 stop_instances method로 변경

<br/>

#### **+추가 : scrapy logger 생성**
> [set_logger.py](https://github.com/aeea-0605/chatbot-repo/blob/main/naver_movie/naver_movie/set_logger.py)
- `LogFilter`
    - 'Scrapying' 문자열이 포함된 로그메세지만 log 파일에 기록
- `ConsoleFilter`
    - console창에 띄울 메세지들을 정의하고 해당 메세지에 대해서만 console창에 띄움
- `make_f_handler`
    - FileHandler 생성 및 log의 format 정의

<br/>

---

### **3-2. 챗봇 서비스 구축**

#### **1) Chatbot Project 생성**
> [setup_chatbot.sh](https://github.com/aeea-0605/chatbot-repo/blob/main/setup_chatbot.sh)
```
$source setup_chatbot.sh
```
- chatbot-repo 디렉토리에서 실행

<br/>

#### **2)chabot.libs modules 작성**
1. `naver.py`
    > [naver.py](https://github.com/aeea-0605/chatbot-repo/blob/main/chatbot/app/libs/naver.py)
    - `translate` : Naver API Key와 텍스트를 받아 번역해주는 함수

2. `forecast.py`
    > [forecast.py](https://github.com/aeea-0605/chatbot-repo/blob/main/chatbot/app/libs/forecast.py)
    - `kakao_local` : Kakao API Key와 지역명을 받아 좌표를 반환하는 함수
    - `weather` : openweathermap API Key와 좌표를 받아 날씨(en)를 반환하는 함수
    - `run` : forecast의 kakao_local, weather 함수와 naver의 translate함수를 순차적으로 실행하여 날씨에 대한 정보를 반환하는 함수

3. `slack.py`
    > [slack.py](https://github.com/aeea-0605/chatbot-repo/blob/main/chatbot/app/libs/slack.py)
    - `send_msg` : Webhook url과 텍스트를 받아 Slack Workspace에 전송해주는 함수

<br/>

#### **3) API KEY와 DB정보에 대한 `config.py` 작성**
> [config.py](https://github.com/aeea-0605/chatbot-repo/blob/main/chatbot/app/config.py)
- data.ini의 "db", "api"에 대한 정보를 불러와 각각 db_info, key_info 변수에 저장
- `Config` : db_info에 대한 정보를 통해 MySQL의 DB와 세션을 연결해주는 Class
- `ApiKey` : key_info에 대한 정보와 해당 정보를 필요에 맞게 반환해주는 static method를 보유한 Class

<br/>

#### **4) app 생성을 위한 `__init__.py` 작성**
> [__init__.py](https://github.com/aeea-0605/chatbot-repo/blob/main/chatbot/app/__init__.py)
- Flask를 사용한 app 생성 및 Config에 대한 정보를 받음
- app.route decorator를 받는 함수들은 import 받아 사용

<br/>

#### **5) naver_movie TABLE과 연결을 위한 `mysql_movie.py` 작성**
> [mysql_movie.py](https://github.com/aeea-0605/chatbot-repo/blob/main/chatbot/app/items/mysql_movie.py)
- app을 import 받아 flask_sqlalchemy를 사용해 app에 연결된 데이터베이스에 naver_movie 테이블 연결

<br/>

#### **6) app의 여러 기능을 위한 `bot.py` 작성**
> [bot.py](https://github.com/aeea-0605/chatbot-repo/blob/main/chatbot/app/routes/bot.py)
- `bot` : Client에게 trigger와 텍스트를 POST 방식으로 request받고 command에 따라 날씨, 번역, 영화순위, 도움말에 대한 정보를 response해주는 함수
    - 날씨 : ApiKey의 static method(get_json)와 naver.run 함수를 사용해 날씨에 대한 정보(korean)를 response
    - 번역 : ApiKey의 get_json과 naver.forecast 함수를 사용해 번역에 대한 정보를 response
    - 영화 : naver_movie TABLE과 연결된 NaverMovie Class와 sqlalchemy를 사용해 영화에 대한 정보를 response
    - 도움 : 챗봇을 이용하는 방법에 대한 정보를 response

<br/>

#### **7) flask를 실행시킬 `chatbot.py` 작성**
> [chatbot.py](https://github.com/aeea-0605/chatbot-repo/blob/main/chatbot/chatbot.py)
- 완성된 app을 import 받아 flask 실행

<br/>

#### **8) Chatbot Project 실행을 위한 `run_chatbot.sh` 작성**
> [run_chatbot.sh](https://github.com/aeea-0605/chatbot-repo/blob/main/run_chatbot.sh)
- Flask Debug를 True로 하여 수정사항에 자동으로 적용되게끔 설정
- `chatbot.py` 를 실행시키는 Shell Script

<br/>

#### **+추가 : chatbot logger 생성**
> [set_logger.py](https://github.com/aeea-0605/chatbot-repo/blob/main/chatbot/app/set_logger.py)
- `Logger`
    - FileHandler가 설정된 logger에 대한 Class

---
---

