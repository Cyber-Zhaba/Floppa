import requests
import sys


def getImage(size, coords, z_scale, map_type, mark=None):
    if mark is None:
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords}&l={map_type}&size={size}&z={z_scale}"
    else:
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords}&l={map_type}&size={size}&z={z_scale}&pt={mark},comma"
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
