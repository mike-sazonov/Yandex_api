from requests import get

def get_response(public_key: str, path: str) -> list:
    params = {"public_key": public_key, "path": path}   # в качестве аргументов для GET запроса к API принимает
    # публичную ссылку и параметр пути
    api_url = "https://cloud-api.yandex.net/v1/disk/public/resources"
    response = get(api_url, params=params).json()["_embedded"]["items"]

    return response # возвращаем список файлов и директорий
