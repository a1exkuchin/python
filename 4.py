# -*- coding: utf-8 -*-
#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
#speed, color, name, is_police (булево). А также методы: go, stop, 
#turn(direction), которые должны сообщать, что машина поехала, остановилась, 
#повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, 
#WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен 
#показывать текущую скорость автомобиля. Для классов TownCar и WorkCar 
#переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 
#40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ 
#к атрибутам, выведите результат. Выполните вызов методов и также покажите 
#результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return print(f'Машина {self.name} поехала')
    def stop(self):
        return print(f'Машина {self.name} остановилась')
    def turn(self, direction):
        if direction == 'left':
            return print(f'Машина {self.name} повернула налево')
        elif direction == 'right':
            return print(f'Машина {self.name} повернула направо')
        else:
            print(f'Данные по направлению машины {self.name} некорректны')
    def show_speed(self):
        return print(f'У машины {self.name} текущая скорость {self.speed} км/ч.')
    def police(self):
        if self.is_police:
            return f'Полицейская машина {self.name}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f'Машина {self.name} превысила скорость, разрешенную для городских машин, на {self.speed - 60} км/ч.')
        else:
            return print(f'У машины {self.name} текущая скорость {self.speed} км/ч.')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f'Машина {self.name} превысила скорость, разрешенную для служебных машин, на {self.speed - 40} км/ч.')
        else:
            return print(f'У машины {self.name} текущая скорость {self.speed} км/ч.')

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

mustang = SportCar(170, 'черный', 'Форд Мустанг', False)
priora = TownCar(70, 'белая', 'Лада Приора', False)
geely = WorkCar(45, 'красная', 'Джили Атлас', False)
focus = PoliceCar(110, 'желтый', 'Форд Фокус', True)

mustang.show_speed()
priora.show_speed()
geely.show_speed()
focus.show_speed()
priora.go()
geely.stop()
mustang.turn('right')
print(f'{focus.police()} на скорости {focus.speed} км/ч преследует {mustang.color} {mustang.name}.')




