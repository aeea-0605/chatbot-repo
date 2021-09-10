import requests


def translate(NAVER_ID, NAVER_SECRET, msg, source="en", target="ko"):
    url = "https://openapi.naver.com/v1/papago/n2mt"
    params = {"source": source, "target": target, "text": msg}
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Naver-Client-Id": NAVER_ID,
        "X-Naver-Client-Secret": NAVER_SECRET
    }
    
    response = requests.post(url, params, headers=headers)
    
    return response.json()['message']['result']['translatedText']