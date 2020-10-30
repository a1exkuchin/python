# -*- coding: utf-8 -*-
#Реализовать функцию int_func(), принимающую слово из маленьких латинских 
#букв и возвращающую его же, но с прописной первой буквой. Например, 
#print(int_func(‘text’)) -> Text

def up_letter(s):
    return s.capitalize()
string = input('Введите строку из слов для обработки: ').split()
print(' '.join(up_letter(word) for word in string))
    