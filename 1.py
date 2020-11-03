#Реализовать функцию, принимающую два числа (позиционные аргументы) и 
#выполняющую их деление. Числа запрашивать у пользователя, предусмотреть 
#обработку ситуации деления на ноль.

def division(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        print('Деление на ноль')
        return
while True:
    try:
        a, b = float(input('Введите делимое: ')), float(input('Введите делитель: '))
        break
    except ValueError:
        print('Вы ввели не число, а что-то другое. Повторите ввод')
        continue
print('Частное равно: ', division(a, b)) 