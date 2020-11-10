# -*- coding: utf-8 -*-
# Реализовать класс Road (дорога), в котором определить атрибуты:
#length (длина), width (ширина). Значения данных атрибутов должны
#передаваться при создании экземпляра класса. Атрибуты сделать
#защищенными. Определить метод расчета массы асфальта, необходимого
# для покрытия всего дорожного полотна. Использовать формулу: длина
# * ширина * масса асфальта для покрытия одного кв метра дороги
# асфальтом, толщиной в 1 см * число см толщины полотна. Проверить
#работу метода.


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

class Road_mass(Road):
    def __init__(self, _length, _width, mass):
        super().__init__(_length, _width)
        self.mass_per_unit_area = mass  
    def get_mass(self, thickness):
        try:
            return (self._length * self._width * thickness * self.mass_per_unit_area)
        except TypeError:
            return None

road = Road_mass(5000, 20, 25)
print('Масса дорожного покрытия составит:', road.get_mass(5)/1000, 'тонн')
