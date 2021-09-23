import requests


def translate(NAVER_ID, NAVER_SECRET, msg, source="en", target="ko"):
    """
    translate function : 번역해주는 함수 (default : English > Korean)
    input arguments : naver_client_id, naver_client_secret, message
                     , source(default : en), target(default : ko)
    return translated message
    """
    url = "https://openapi.naver.com/v1/papago/n2mt"
    params = {"source": source, "target": target, "text": msg}
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Naver-Client-Id": NAVER_ID,
        "X-Naver-Client-Secret": NAVER_SECRET
    }
    
    response = requests.post(url, params, headers=headers)
    
    return response.json()['message']['result']['translatedText']