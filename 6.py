# -*- coding: utf-8 -*-
from itertools import count
from itertools import cycle
k = int(input('Введите целое число, меньшее 40: '))
for num in count(k):
    if num > 40:
        break
    else:
        print(num, end=' ')
l = input('Введите строку символов: ')
c = 0
for char in cycle(l):
    if c > 40:
        break
    print(char, end=' ')
    c += 1
