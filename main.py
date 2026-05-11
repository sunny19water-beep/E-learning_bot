import os
import requests
from dotenv import load_dotenv

load_dotenv()

LINE_TOKEN = os.getenv("LINE_TOKEN")
USER_ID = os.getenv("USER_ID")

url = "https://api.line.me/v2/bot/message/push"

headers = {
    "Authorization": f"Bearer {LINE_TOKEN}",
    "Content-Type": "application/json"
}

data = {
    "to": USER_ID,
    "messages": [
        {
            "type": "text",
            "text": "e-learningがまもなく終了します"
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.text)