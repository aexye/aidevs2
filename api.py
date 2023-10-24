import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("AIDEVS_API")
url = 'https://zadania.aidevs.pl/token/'


def get_token(task_name):
    task_url = url + task_name
    r = requests.post(task_url, json={api_key: api_key})
    if response.status_code == 200:
        if response.text.strip():
            data = response.json()
            return data


auth = get_token('helloapi')
print(auth)