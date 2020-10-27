# -*- coding: utf-8 -*-
#Реализовать структуру данных «Товары». Она должна представлять собой список 
#кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже
#должно быть два элемента — номер товара и словарь с параметрами 
#(характеристиками товара: название, цена, количество, единица измерения).
#Структуру нужно сформировать программно, т.е. запрашивать все данные у 
#пользователя.

product_list = list()
index=1
while True:
    if input('Вы хотите ввести данные о товаре? (д/н) ').lower() == 'д':
        product=dict()
        product['название'] = input('Введите название товара ')
        try:
            product['цена'] = int(input('Введите цену товара '))
        except BaseException:
            print('Вы ввели текст, а надо было ввести число' )
            continue
        try:
            product['количество'] = int(input('Введите количество товара '))
        except BaseException:
            print('Вы ввели текст, а надо было ввести число' )
            continue
        product['ед'] = input('Введите единицы измерения товара ')  
        goods_record = tuple((index, product))
        product_list.append(goods_record)
        index+=1
    else:
        break
slice_name = set()
slice_cost = set()
slice_amt = set()
slice_units = set()
for element in product_list:
    slice_name.add(element[1]['название'])
    slice_cost.add(element[1]['цена']) 
    slice_amt.add(element[1]['количество'])
    slice_units.add(element[1]['ед'])
slices = {'название' : list(slice_name), 'цена' : list(slice_cost), 
          'количество' : list(slice_amt),  'ед' : list(slice_units)}
print(slices)
    