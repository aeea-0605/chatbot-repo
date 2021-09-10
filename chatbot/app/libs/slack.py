import requests, json


def send_msg(WEBHOOK_URL, msg, channel="#dss", username="bot"):
    payload = {"channel": channel, "username": username, "text": msg}
    
    return requests.post(WEBHOOK_URL, json.dumps(payload))