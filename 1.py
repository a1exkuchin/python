# -*- coding: utf-8 -*-
#Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
#(метод __init__()), который должен принимать данные (список списков) для 
#формирования матрицы.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы 
#в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции 
#сложения двух объектов класса Matrix (двух матриц). Результатом сложения 
#должна быть новая матрица.
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])
    def __add__(self, other):
        n, m = self.size()
        row = []
        col = []
        for i in range(n):
            for j in range(m):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            col.append(row)
            row = []
        return Matrix(col)   
    def size(self):
        return (len(self.matrix), len(self.matrix[0]))    
    
a = Matrix([[1000, 10, 100], [2, -55555, 60], [230, 5, -56], [2, 2, 2]])
b = Matrix([[-1000, 10, -100], [2, 55555, 60], [230, -5, 56], [-2, 0, 0]])
c = Matrix([[0, 10, -100], [2, 0, 60], [23, -5, 56], [-2, 0, 0]])
print(a.size())
print(a)
print()
print(b)
print()
print(a + b)
print()
print(a + b + c)

