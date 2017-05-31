#!/usr/bin/env python3

import json
from pathlib import Path
top = Path(__file__).resolve().parents[0].as_posix()

from urllib import request

import logging
import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)

class WeatherInfo:

    def __init__(self, openweathermap_key: str, cities_file_name: str=top + '/' + 'cities.txt'):
        '''
        Constructor
        Args:
            openweathermap_key: openweathermap.org api key (https://openweathermap.org/)
            cities_file_name: cities ids database file name
        '''

        self.cities = dict()

        self.key = openweathermap_key

        try:
            self.cities = json.load(open(cities_file_name, 'r'))
        except Exception as e:
            logging.error(str(e))

    def _wind_direction(self, deg: int) -> str:
        deg %= 360
        if deg > 300 or deg < 30:
            return 'северный'
        elif deg < 70:
            return 'северо-западный'
        elif deg < 105:
            return 'западный'
        elif deg < 165:
            return 'юго-западный'
        elif deg < 195:
            return 'южный'
        elif deg < 255:
            return 'юго-восточный'
        elif deg < 285:
            return 'восточный'
        else:
            return 'северо-восточный'

    def get_weather(self, city_name='Москва'):
        '''
        Get weather information
        Args:
            city_name: name of city
        Returns:
            weather information in format:
                dictionary = {
                    'temp': temperature,
                    'pressure': pressure,
                    'humidity': humidity,
                    'wind_speed': wind_speed,
                    'wind_speed': wind_direction
                }
        '''
        if len(self.cities) > 0:
            city_id = self.cities.get(city_name.lower().strip())
            if city_id is not None:
                url = 'http://api.openweathermap.org/data/2.5/weather?id=' + \
                      str(list(city_id.values())[0]) + '&appid=' + self.key + \
                      '&units=metric'

                try:
                    req = request.urlopen(url)
                    info = json.loads(req.read().decode('utf-8'))
                    weather = info['main']

                    weather_info = dict()
                    weather_info['temp'] = weather['temp']
                    weather_info['pressure'] = weather['pressure']
                    weather_info['humidity'] = weather['humidity']
                    weather_info['wind_speed'] = info['wind']['speed']
                    weather_info['wind_direction'] = self._wind_direction(info['wind']['deg'])

                    return weather_info
                except Exception as e:
                    logging.error(str(e))
                    print(str(e))
                    return None