from requests import get

def get_response():
    params = {"public_key": "https://disk.yandex.ru/d/noSJtVxwQ99P4A",
              "path": "/"}
    response = get("https://cloud-api.yandex.net/v1/disk/public/resources", params=params)

    return response.json()["_embedded"]["items"]
