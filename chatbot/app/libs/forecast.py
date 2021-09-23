import requests
from app.libs import naver


def kakao_local(KAKAO_KEY, addr):
    """
    kakao_local function : 특정 지역에 대한 좌표를 제공해주는 함수
    input arguments : kakao_rest_api_key, region(korean) 
    return lat, lon (about region)
    """
    
    url = f"https://dapi.kakao.com/v2/local/search/address.json?query={addr}"
    headers = {"Authorization": f"KakaoAK {KAKAO_KEY}"}
    
    response = requests.get(url, headers=headers)
    location = response.json()['documents'][0]
    
    return location['y'], location['x']


def weather(WEATHER_KEY, lat, lon):
    """
    weather function : 좌표에 대한 날씨 정보를 제공해주는 함수
    input arguments : openweathermap_api_key, latitude, longitude
    return current hourly weather in English
    """
    
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&lang=en&exclude=hourly&appid={WEATHER_KEY}"
    response = requests.get(url)
    
    return response.json()['current']['weather'][0]['description']


def run(NAVER_ID, NAVER_SECRET, KAKAO_KEY, WEATHER_KEY, addr):
    """
    run function : kakao_local, weather, translate 를 콜백함수로 받아
                   최종적으로 특정 지역에 대한 날씨 정보를 제공해주는 함수
    input argument : naver_client_id, naver_client_secret, kakao_rest_api_key
                    , openweatermap_api_key, region
    return current hourly weather in Korean
    """
    lat, lon = kakao_local(KAKAO_KEY, addr)
    msg_en = weather(WEATHER_KEY, lat, lon)
    msg_ko = naver.translate(NAVER_ID, NAVER_SECRET, msg_en)
    
    return f"{addr}의 날씨는 '{msg_ko}({msg_en})'입니다."