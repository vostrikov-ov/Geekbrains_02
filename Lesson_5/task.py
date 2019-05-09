#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1. Создайте класс Word.
2. Добавьте свойства text и part of speech.
3. Добавьте возможность создавать объект слово со значениями в скобках.
4. Создайте класс Sentence
5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
6. Добавьте метод show, составляющий предложение.
7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.
'''
from random import choice, randint


class Word:
    text = None
    part_of_speech = None

    def __init__(self, text, part_of_speech):
        self.text = text
        self.part_of_speech = part_of_speech.split(':')

    def show(self):
        try:
            x, y = self.part_of_speech
            x = int(x) if x.isdigit() else None
            y = int(y) if y.isdigit() else None
            print(f'Исходное слово: {self.text}')
            print(f'Выбранный фрагмент: {self.text[x:y]}\n')
        except:
            print('Вы указали неправильный диапазон')


class Sentence:
    sentence = None

    # Урок №6
    # 4. Перестройте работу метода show класса Sentence.
    # 5. Перестройте работу метода show_part класса Sentence, чтобы он показывал грамматические характеристики.
    #

    def __init__(self, text, content):
        self.text = text
        self.content = content

    def show(self):
        words = []
        for x in self.content:
            words.append(self.text[x][0])
        print('Составленное предложение:')
        print((' '.join(words)).capitalize())

    def show_parts(self):
        finded_parts = []
        for x in self.content:
           finded_parts.append(self.text[x][1])
        finded_parts = set(finded_parts)
        print('Грамматические хакартеристики:')
        print(*finded_parts, sep=', ')


if __name__ == '__main__':

    slovo = Word('Первомай', '5:8')
    slovo.show()

    slovo2 = Word('Зеленое яблоко', '0:7')
    slovo2.show()

    text = [
        ('Съешьте', 'глагол'), ('еще', 'наречие'), ('этих', 'местоимение'),
        ('мягких', 'прилагательное'), ('французских', 'прилагательное'),
        ('булок,', 'существительное'), ('да', 'союз'), ('выпейте', 'глагол'),
        ('же', 'частица'), ('чаю', 'существительное')
    ]
    numbers = [0, 2, 4, 5]

    test_text = Sentence(text, numbers)
    test_text.show()
    test_text.show_parts()
