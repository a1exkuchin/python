# -*- coding: utf-8 -*-
#Программа принимает действительное положительное число x и целое отрицательное 
#число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо 
#реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись 
#без встроенной функции возведения числа в степень.

def my_func(x, y):
    #x>0, y in Z, y<0
    prod = 1
    for i in range(abs(y)):
        prod*=x
    return 1/prod
while True: 
    try:
        x = float(input('Введите положительное число: '))
        if x <= 0:
            print('Вы вввели что-то не то, попробуйте ещё раз.')
            continue
        y = int(input('Введите отрицательное целое число: '))
        if y >= 0:
            print('Вы вввели что-то не то, попробуйте ещё раз.')
            continue
        break
    except ValueError:
        print('Вы вввели что-то не то, попробуйте ещё раз.')
        continue
print(my_func(x, y))
