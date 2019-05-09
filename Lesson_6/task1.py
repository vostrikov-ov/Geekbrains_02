#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1. Создайте классы Noun и Verb.
2. Настройте наследование от Word.
3. Добавьте защищенное свойство «Грамматические характеристики».
4. Перестройте работу метода show класса Sentence.
5. Перестройте работу метода show_part класса Sentence, чтобы он показывал грамматические характеристики.
'''
import sys

sys.path.append('../Lesson_5')
from task import Word


class Noun(Word):
    _gram_char = ''

class Verb(Word):
    _gram_char = ''

