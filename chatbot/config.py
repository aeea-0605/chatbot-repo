import configparser


config = configparser.ConfigParser()
config.read("../data.ini")
info = config['api']

class Config(object):
    DEBUG = True
    TEMTLATES_AUTO_RELOAD = True
    
    KAKAO_KEY = info['KAKAO_KEY']
    WEATHER_KEY = info['WEATHER_KEY']
    NAVER_ID = info['NAVER_ID']
    NAVER_SECRET = info['NAVER_SECRET']
    WEBHOOK_URL = info['WEBHOOK_URL']
    
    @staticmethod
    def get_json(need_list):
        data = {}
        if "kakao" in need_list:
            data.update({"KAKAO_KEY": Config.KAKAO_KEY})
        if "weather" in need_list:
            data.update({"WEATHER_KEY": Config.WEATHER_KEY})
        if "naver" in need_list:
            data.update({"NAVER_ID": Config.NAVER_ID, "NAVER_SECRET": Config.NAVER_SECRET})
        
        return data