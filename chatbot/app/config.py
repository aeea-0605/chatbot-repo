import configparser


config = configparser.ConfigParser()
config.read("../data.ini")
key_info = config['api']
db_info = config['db']

class Config(object):
    """
    Config Class : mysql의 db와 세션을 연결해주는 Class
    """
    TEMTLATES_AUTO_RELOAD = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_info["USER"]}:{db_info["PASSWORD"]}@{db_info["HOST"]}/{db_info["DB"]}'


class ApiKey:
    """
    ApiKey Class : 챗봇의 내부적인 기능을 수행하기 위해 필요한
                   api_key 및 webhook_url 정보와 함수가 있는 Class
    Static Method
        get_json function : list타입으로 필요한 class variable을 입력하면
                            dictionary 타입으로 해당 정보를 리턴해주는 함수
        input arguments : need_list (필요한 api의 이름)
        return api_key to json
    """
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