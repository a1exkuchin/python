# -*- coding: utf-8 -*-
#Пользователь вводит время в секундах. Переведите время в часы, минуты и 
#секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
sec=int(input('Введите время в секундах: '))
hours=sec//3600
sec=sec%3600
minutes=sec//60
sec=sec%60
print ('%(hours)02d:%(minutes)02d:%(sec)02d' % {"hours": hours, "minutes": minutes, "sec": sec})
