#����������� ������� my_func(), ������� ��������� ��� ����������� ���������, � 
#���������� ����� ���������� ���� ����������.

def my_func(a, b, c):
    return a + b + c - min(a, b, c)
while True: 
    try:
        a, b, c = map(float, input('������� ��� ����� ����������� ��������: ').split())
        break
    except ValueError:
        print('�� ������ �� �����')
        continue
print('������� �������� �����: ', my_func(a, b, c))
 
