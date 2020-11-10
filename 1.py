# -*- coding: utf-8 -*-
#Создать класс TrafficLight (светофор) и определить у него один атрибут 
#color (цвет) и метод running (запуск). Атрибут реализовать как приватный. 
#В рамках метода реализовать переключение светофора в режимы: красный, 
#желтый, зеленый. Продолжительность первого состояния (красный) составляет 
#7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше 
#усмотрение.#Переключение между режимами должно осуществляться только в 
#указанном порядке (красный, желтый, зеленый). Проверить работу примера, 
#создав экземпляр и вызвав описанный метод.

from time import sleep

class TrafficLight():
    __color = {'red':7, 'yellow':2, 'green':8}
    def running(self):
        for key in TrafficLight.__color.keys():
            print(key)
            sleep(TrafficLight.__color[key])

lighter = TrafficLight()
print('For quit press Ctrl+C')
while True:
    try:
        lighter.running()
    except KeyboardInterrupt:
        break