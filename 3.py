# -*- coding: utf-8 -*-
#Реализовать функцию my_func(), которая принимает три позиционных аргумента, и 
#возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    return a + b + c - min(a, b, c)
while True: 
    try:
        a, b, c = map(float, input('Введите три числа разделенные пробелом: ').split())
        break
    except ValueError:
        print('Вы вввели не числа')
        continue
print('Искомое значение равно: ', my_func(a, b, c))
 
