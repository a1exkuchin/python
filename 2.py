# -*- coding: utf-8 -*-
#Создать текстовый файл (не программно), сохранить в нем несколько строк, 
#выполнить подсчет количества строк, количества слов в каждой строке.

f = open('test.txt')
content = f.readlines()
print('Количество строк в файле: ', len(content))
i = 1
for string in content:
    print(str(len(string.split())) + ' слова(о) в ' + str(i) + ' строке')
    i +=1
f.close()
