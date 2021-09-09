from flask import *

import libs.naver as naver
import libs.forecast as forecast
import libs.slack as slack
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    return "server is running!"


@app.route("/bot", methods=["POST"])
def bot():
    trigger_word = request.form.get('trigger_word')
    text = request.form.get('text')
    text = text.replace(trigger_word, "").strip()
    
    if text.find(":") <= 0:
        msg = "[command]:[data] 포맷으로 입력해주세요."
        slack.send_msg(Config.WEBHOOK_URL, msg)
        return Response(), 200
    
    command, data = text.split(":")[0], text.split(":")[1]
    if command == "날씨":
        params = Config.get_json(["naver", "kakao", "weather"])
        params.update({"addr": data})
        msg = forecast.run(**params)
    elif command == "번역":
        params = Config.get_json(["naver"])
        params.update({"msg": data})
        msg = naver.translate(**params)
    else:
        msg = f'{command}는 없는 명령입니다. 현재 가능한 명령어는 날씨, 번역 입니다.'
        
    slack.send_msg(Config.WEBHOOK_URL, msg)
    return Response(), 200

app.run()