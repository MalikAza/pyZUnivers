import requests

API_BASE_URL = "https://zunivers-api.zerator.com/public"
PLAYER_BASE_URL = "https://zunivers.zerator.com/joueur"
FULL_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

class ZUniversAPIError(Exception):
    def __init__(self, url) -> None:
        self.url = url
        self.message = 'Something went wrong on ZUnivers API.'

    def __str__(self) -> str:
        return f'{self.message} EndPoint: {self.url}'

def get_datas(url):
    with requests.get(url) as resp:
        try:
            datas = resp.json()
        except Exception as e:
            if type(e).__name__ == 'JSONDecodeError': raise ZUniversAPIError(url)
            else: raise e

    return datas