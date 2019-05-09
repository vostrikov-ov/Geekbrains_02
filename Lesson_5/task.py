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

    def __init__(self, text):
        self.text = text.split()
        self.content = list(range(len(self.text)))

    def show(self):
        words = []
        text_copy = self.text.copy()
        for x in range(randint(1, len(self.text))):
            word = choice(text_copy)
            words.append(word)
            text_copy.remove(word)
        self.sentence = ' '.join(words)

    def show_parts(self):
        finded_parts = []
        sentence_parts = self.sentence.split()
        for num_part in self.content:
            if self.text[num_part] in sentence_parts:
                finded_parts.append(num_part)
        print('В составном прежложении содержатся слова исходного предложения, со следующими номерами:')
        print(*finded_parts, sep=', ')


if __name__ == '__main__':

    slovo = Word('Первомай', '5:8')
    slovo.show()

    slovo2 = Word('Зеленое яблоко', '0:7')
    slovo2.show()

    test_text = Sentence('добавьте возможность создавать объект слово со значениями в скобках')
    test_text.show()
    print(f'Составленное предложение: {test_text.sentence}')
    test_text.show_parts()
