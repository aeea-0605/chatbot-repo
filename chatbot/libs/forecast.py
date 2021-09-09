import requests
import libs.naver as naver


def kakao_local(KAKAO_KEY, addr):
    """
    return lat, lon
    """
    
    url = f"https://dapi.kakao.com/v2/local/search/address.json?query={addr}"
    headers = {"Authorization": f"KakaoAK {KAKAO_KEY}"}
    
    response = requests.get(url, headers=headers)
    location = response.json()['documents'][0]
    
    return location['y'], location['x']


def weather(WEATHER_KEY, lat, lon):
    """
    return current hourly weather in English
    """
    
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&lang=en&exclude=hourly&appid={WEATHER_KEY}"
    response = requests.get(url)
    
    return response.json()['current']['weather'][0]['description']


def run(NAVER_ID, NAVER_SECRET, KAKAO_KEY, WEATHER_KEY, addr):
    lat, lon = kakao_local(KAKAO_KEY, addr)
    msg_en = weather(WEATHER_KEY, lat, lon)
    msg_ko = naver.translate(NAVER_ID, NAVER_SECRET, msg_en)
    
    return f"{addr}의 날씨는 '{msg_ko}({msg_en})'입니다."