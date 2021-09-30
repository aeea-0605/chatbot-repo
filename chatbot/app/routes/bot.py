import os
import logging
from flask import request, Response
from app import app
from app.libs import naver
from app.libs import forecast
from app.libs import slack
from app.config import ApiKey
from app.items.mysql_movie import NaverMovie
from app.set_logger import Logger


save_path = os.path.join(os.getcwd(), 'log')

logger = Logger('chatbot', save_path)

@app.route("/")
def index():
    return "server is running!"


@app.route("/bot", methods=["POST"])
def bot():
    trigger_word = request.form.get('trigger_word')
    text = request.form.get('text')
    text = text.replace(trigger_word, "").strip()

    if text.find(":") <= 0:
        msg = '[command]:[data] 포맷으로 입력해주세요. \n챗봇의 기능을 알고싶다면 "$bot 도움:" 을 입력해주세요.'
        slack.send_msg(ApiKey.WEBHOOK_URL, msg)
        return Response(), 200

    command, data = text.split(":")[0], text.split(":")[1]

    logger.logger.info(f"@@command: {command} @@data: {data}")

    if command == "날씨":
        params = ApiKey.get_json(["naver", "kakao", "weather"])
        params.update({"addr": data})
        msg = forecast.run(**params)
    elif command == "번역":
        params = ApiKey.get_json(["naver"])
        params.update({"msg": data})
        msg = naver.translate(**params)
    elif command == "영화":
        if data != "전체":    
            datas = NaverMovie.query.order_by(NaverMovie.rate.desc()).limit(int(data)).all()
        else:
            datas = NaverMovie.query.order_by(NaverMovie.rate.desc()).all()
            
        msg = f'<수집시점 : {datas[0].crawled_time.split(" ")[0]}>\n'
        for i in range(int(datas)):
            msg += f'{i+1}. {datas[i].title} (예매율: {datas[i].rate}%, 평점: {datas[i].score}) \n'
            msg += f'\t {datas[i].link}\n'
            if i != (int(datas) - 1):
                msg += "-------------------\n"
    elif command == "도움":
        msg = """
챗봇 실행 명령어 >> $bot [command]:[data]
command : 날씨, data : 날씨를 알고 싶은 지역명
command : 번역, data : 번역하고 싶은 영문(english > korean)
command : 영화, data : 현재상영작 중 보고 싶은 마지막 순위 입력
        """
    else:
        msg = f'{command}는 없는 명령입니다. 현재 가능한 명령어는 날씨, 번역, 영화, 도움 입니다.'

    slack.send_msg(ApiKey.WEBHOOK_URL, msg)
    return Response(), 200