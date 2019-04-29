#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Написать функцию получения IATA-кода города из его названия, используя API Aviasales.
'''
import requests
import json

city = input('Введите название города: ')

link = 'http://autocomplete.travelpayouts.com/places2?term={}&locale=ru&types[]=city'

result = requests.get(link.format(city)).text
iata_code = json.loads(result)[0]['code']

print('IATA код города {} - {}'.format(city, iata_code))
