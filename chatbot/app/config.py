import configparser


config = configparser.ConfigParser()
config.read("../data.ini")
key_info = config['api']
db_info = config['db']

class Config(object):
    # DEBUG = True
    TEMTLATES_AUTO_RELOAD = True
    TEMTLATES_AUTO_RELOAD = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_info["USER"]}:{db_info["PASSWORD"]}@{db_info["HOST"]}/{db_info["DB"]}'


class ApiKey:    
    KAKAO_KEY = key_info['KAKAO_KEY']
    WEATHER_KEY = key_info['WEATHER_KEY']
    NAVER_ID = key_info['NAVER_ID']
    NAVER_SECRET = key_info['NAVER_SECRET']
    WEBHOOK_URL = key_info['WEBHOOK_URL']
    
    @staticmethod
    def get_json(need_list):
        data = {}
        if "kakao" in need_list:
            data.update({"KAKAO_KEY": ApiKey.KAKAO_KEY})
        if "weather" in need_list:
            data.update({"WEATHER_KEY": ApiKey.WEATHER_KEY})
        if "naver" in need_list:
            data.update({"NAVER_ID": ApiKey.NAVER_ID, "NAVER_SECRET": ApiKey.NAVER_SECRET})
        
        return data