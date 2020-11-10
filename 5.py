# -*- coding: utf-8 -*-
#Реализовать класс Stationery (канцелярская принадлежность). Определить в нем 
#атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение 
#“Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil 
#(карандаш), Handle (маркер). В каждом из классов реализовать переопределение 
#метода draw. Для каждого из классов методы должен выводить уникальное 
#сообщение. Создать экземпляры классов и проверить, что выведет описанный 
#метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return print('Запуск отрисовки')

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return print(f'Запускаем {self.title}. Рисуем ручкой.')

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return print(f'Запускаем {self.title}. Рисуем карандашом.')

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return print(f'Запускаем {self.title}. Рисуем маркером.')

pen = Pen('ручку')
pencil = Pencil('карандаш')
handle = Handle('маркер')
pen.draw()
pencil.draw()
handle.draw()