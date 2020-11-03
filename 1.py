#����������� �������, ����������� ��� ����� (����������� ���������) � 
#����������� �� �������. ����� ����������� � ������������, ������������� 
#��������� �������� ������� �� ����.

def division(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        print('������� �� ����')
        return
while True:
    try:
        a, b = float(input('������� �������: ')), float(input('������� ��������: '))
        break
    except ValueError:
        print('�� ����� �� �����, � ���-�� ������. ��������� ����')
        continue
print('������� �����: ', division(a, b)) 