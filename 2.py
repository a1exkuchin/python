# -*- coding: utf-8 -*-
#Реализовать проект расчета суммарного расхода ткани на производство одежды. 
#Основная сущность (класс) этого проекта — одежда, которая может иметь 
#определенное название. К типам одежды в этом проекте относятся пальто и 
#костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост 
#(для костюма). Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: 
#для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих
#методов на реальных данных. Реализовать общий подсчет расхода ткани. 
#Проверить на практике полученные на этом уроке знания: реализовать 
#абстрактные классы для основных классов проекта, проверить на практике 
#работу декоратора @property.
from abc import ABC, abstractmethod

class AbsractWear(ABC):
    @abstractmethod
    def square(self):
        pass

class Wear(AbsractWear):
    def __init__(self, wtype, size):
        self.wtype = wtype
        self.size = size
    @property
    def square(self):
        if self.wtype == 'coat':
            return self.size / 6.5 + 0.5
        elif self.wtype == 'suit':
            return self.size * 2 + 0.3
        else:
            return 0

coat1 = Wear('coat', 1.2)
print('Расход ткани на пальто равен: ', '%.3f' % coat1.square)
suit1 = Wear('suit', 1.05)
print('Расход ткани на костюм равен: ', '%.3f' % suit1.square)
coat2 = Wear('coat', 2.1)
suit2 = Wear('suit', 1.05)
print('Общий расход ткани равен: ', '%.3f' % (coat1.square + suit1.square + coat2.square + suit2.square))

