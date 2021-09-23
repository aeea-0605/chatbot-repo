import requests, json


def send_msg(WEBHOOK_URL, msg, channel="#dss", username="bot"):
    """
    send_msg function : 메세지를 slack work space에 전송해주는 함수
    input arguments : slack_webhook_url, message
                     , channel(default : #dss), username(default : bot)
    return <Response [200]>, if send_msg succeed.
    """
    payload = {"channel": channel, "username": username, "text": msg}
    
    return requests.post(WEBHOOK_URL, json.dumps(payload))