# -*- coding: utf-8 -*-
#Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую 
#построчно данные. При этом английские числительные должны заменяться на 
#русские. Новый блок строк должен записываться в новый текстовый файл.

number = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
with open('numbers.txt') as f_in:
    f_out = open('num_out.txt', 'w')
    for string in f_in:
        for key in number:
            if key in string:
                f_out.write(string.replace(key, number[key]))
    f_out.close()    