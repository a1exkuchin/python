# -*- coding: utf-8 -*-
#Создать (программно) текстовый файл, записать в него программно набор чисел, 
#разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и 
#выводить ее на экран.
from random import randint
with open('numbers.txt', 'w') as f_out:
    for i in range(300):
        f_out.write(str(randint(1, 100))+' ')
with open('numbers.txt') as f_in:
    numbers = map(int, f_in.read().split())
summ = 0
for i in numbers:
    summ += i
print('Сумма чисел из файла', f_out.name, 'равна: ', summ)     
