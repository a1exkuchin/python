# -*- coding: utf-8 -*-
#������� ����� TrafficLight (��������) � ���������� � ���� ���� ������� 
#color (����) � ����� running (������). ������� ����������� ��� ���������. 
#� ������ ������ ����������� ������������ ��������� � ������: �������, 
#������, �������. ����������������� ������� ��������� (�������) ���������� 
#7 ������, ������� (������) � 2 �������, �������� (�������) � �� ���� 
#����������.#������������ ����� �������� ������ �������������� ������ � 
#��������� ������� (�������, ������, �������). ��������� ������ �������, 
#������ ��������� � ������ ��������� �����.

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