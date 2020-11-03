# -*- coding: utf-8 -*-
#Представлен список чисел. Необходимо вывести элементы исходного списка, 
#значения которых больше предыдущего элемента.

source = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
destination = [source[i] for i in range(1,len(source)) if source[i] > source[i-1]]
print(' '.join(map(str,destination)))