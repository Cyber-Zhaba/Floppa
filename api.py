import requests
import sys


def getImage(size, coords):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords}&spn=0.002,0.002&l=map&size={size}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    return map_file
