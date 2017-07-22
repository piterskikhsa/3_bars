import json
import os
from math import fabs


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    return max(data, key=lambda d: d['SeatsCount'])



def get_smallest_bar(data):
    return min(data, key=lambda d: d['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    bar = {}
    for item in data:
        if not bar:
            bar = item
            continue
        if fabs(float(item['Latitude_WGS84']) - latitude) <= fabs(float(bar['Latitude_WGS84'])-latitude) and \
                fabs(float(item['Longitude_WGS84']) - longitude) <= fabs(float(bar['Longitude_WGS84'])-longitude):
            bar = item
    return bar

if __name__ == '__main__':
    file_path = input('ВВедите путь к файлу')
    json_content = load_json_data(file_path)
    if json_content:
        print('Данные упешно загружнны!')
        answer = int(input('''
        Выбирете вариант действия:
        1. Самый большой бар.
        2. Самый маленький бар.
        3. Самый близкий бар. 
        4. Выйти.
        '''))
        if answer == 1:
            print(get_biggest_bar(json_content))
        elif answer == 2:
            print(get_smallest_bar(json_content))
        elif answer == 3:
            x,y = float(input("ВВедите ваши координаты(долгота, широта)"))
            print(get_closest_bar(json_content, x, y))
        else:
            print("До свидания")
    else:
        print('Ошибка загрузки данных')
