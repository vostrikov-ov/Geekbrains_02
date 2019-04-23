#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1. Получить количество учеников с сайта geekbrains.ru:
a) при помощи регулярных выражений,
b) при помощи библиотеки BeautifulSoup.
'''
import re
from bs4 import BeautifulSoup as BS


# Вариант A
with open('index.html') as f:
    html_text = f.read()

regex = '<span class=\"total-users\">\D+([\d ]+)\D+<'
students = re.findall(regex, html_text)
students = students[0].replace(' ', '')
print('Вариант А:', students, 'учеников')


# Вариант B
soup = BS(html_text, 'html.parser')
text = soup.find('span', {'class': 'total-users'}).string
students = [x for x in text.split() if x.isdigit()]
print('Вариант B: {} учеников'.format(''.join(students)))
