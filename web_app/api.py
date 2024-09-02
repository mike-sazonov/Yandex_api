from requests import get

def get_response(public_key):
    params = {"public_key": public_key,
              "path": "/"}
    response = get("https://cloud-api.yandex.net/v1/disk/public/resources", params=params)

    return response.json()["_embedded"]["items"]
