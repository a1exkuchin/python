#����������� �������, ����������� ��������� ����������, ����������� ������ 
#������������: ���, �������, ��� ��������, ����� ����������, email, �������. 
#������� ������ ��������� ��������� ��� ����������� ���������. ����������� 
#����� ������ � ������������ ����� �������.
def contact(name, surname, year, town, email, phone):
    print(f"������������: {surname} {name}, ��� ��������: {year}, ����� ����������: {town}, �����: {email}, �������: {phone} ")
 
contact(name = input('������� ��� ������������: '), surname = input('������� ������� ������������: '),  
        year = input('������� ��� ��������: '), town = '������', email = input('������� email: '), 
        phone = input('������� �������: ') )