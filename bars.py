import json
import os
from math import sqrt

import sys


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(json_data):
    return max(json_data, key=lambda bar: bar['SeatsCount'])


def get_smallest_bar(json_data):
    return min(json_data, key=lambda bar: bar['SeatsCount'])


def get_closest_bar(json_data, longitude, latitude):
    return min(json_data, key=lambda bar: get_distance(bar['Longitude_WGS84'], bar['Latitude_WGS84'], longitude, latitude) )

def get_distance(bar_longitude, bar_latitude, user_longitude, user_latitude):
    return sqrt((float(bar_latitude) - float(user_latitude))**2 + (float(bar_longitude) - float(user_longitude))**2)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input('ВВедите путь к файлу: ')

    json_content = load_json_data(file_path)

    if json_content:
        print('Самый большой бар - ', get_biggest_bar(json_content)['Name'])
        print('Самый маленький бар - ', get_smallest_bar(json_content)['Name'])

        print('Введите ваши координаты')
        user_longitude = input('Долгота: ')
        user_latitude = input('Широта: ')

        if user_latitude and user_longitude:
            print('Самый близкий бар - ', get_closest_bar(json_content, user_longitude, user_latitude)['Name'])
        else:
            print('Координаты не заданы')
    else:
        print('Ошибка загрузки данных')
