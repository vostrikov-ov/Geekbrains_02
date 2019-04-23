#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1. Получите текст из файла.
2. Разбейте текст на предложения.
3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
4. Отберите все ссылки.
5. Ссылки на страницы какого домена встречаются чаще всего?
6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
'''
import  re
from pprint import pprint


# Считываем текст из файла
textfile = 'text'
with open(textfile) as f:
    task_text = f.read()

# Разбиваем текст на предложения
task_text = re.split('\.\s', task_text)

# Ищем русские слова из 4 и более букв
words = []
regex = re.compile('[А-Яа-я]{4,}')
for sentence in task_text:
    words += regex.findall(sentence)

# Приводим слова к одному регистру
words = [x.lower() for x in words]

# Ищем самое используемое слово.
# Вариант 1 поиска самого повторяющегося элемента списка
words_set = set(words)
popular_words = {}
for word in words_set:
    popular_words[word] = words.count(word)
popular_words = sorted(popular_words.items(), reverse=True, key=lambda x: x[1])
print('{:=^60}'.format(' ТОП 5 самых используемых слов: '))
print('-' * 60)
print('{:<40} | {}'.format('Слово', 'Кол-во повторений'))
print('-' * 60)
for word, num in popular_words[:5]:
    print('{:<40} : {}'.format(word, num))

# Находим все ссылки
links = []
regex = re.compile('[A-Za-z0-9\.\/]+[a-z0-9]')
for sentence in task_text:
    links += regex.findall(sentence)

# Приводим ссылки к одному регистру
links = [x.lower() for x in links]

# Ищем самый популярный домен
# Вариант 2 поиска самого повторяющегося элемента списка
domains = []
for link in links:
    domains.append(link.split('/')[0])
popular_domain = max(domains, key=domains.count)
print('\nСамый популярный домен:', popular_domain)

# Заменяем все ссылки на текст
text_wo_links = []
regex = re.compile('[A-Za-z0-9\.\/]+[a-z0-9]')
for sentence in task_text:
    text_wo_links.append(regex.sub('«Ссылка отобразится после регистрации»', sentence))
print(text_wo_links)
