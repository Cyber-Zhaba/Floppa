import pprint

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


def findObject(text):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={text}&format=json"
    response = requests.get(geocoder_request)
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"].replace(' ', ',')
    return toponym_coodrinates, toponym_coodrinates, toponym['metaDataProperty']['GeocoderMetaData']['text']


def GetPostIndex(text):
    try:
        geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={text}&format=json"
        response = requests.get(geocoder_request)
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        try:
            code = toponym['metaDataProperty']["GeocoderMetaData"]['Address']['postal_code']
        except KeyError:
            code = None
        return code
    except KeyError:
        return None
