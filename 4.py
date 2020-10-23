# -*- coding: utf-8 -*-
#Пользователь вводит целое положительное число. Найдите самую большую 
#цифру в числе. Для решения используйте цикл while и арифметические операции.

number=int(input('Введите целое положительное число: '))
maximum=0
while number>0:
    if maximum<number%10:
        maximum=number%10
    else:
        number=number//10
print('Максимальная цифра введенного числа: ', maximum)
