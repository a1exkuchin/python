#����������� ������� int_func(), ����������� ����� �� ��������� ��������� 
#���� � ������������ ��� ��, �� � ��������� ������ ������. ��������, 
#print(int_func(�text�)) -> Text

def up_letter(s):
    return s.capitalize()
string = input('������� ������ �� ���� ��� ���������: ').split()
print(' '.join(up_letter(word) for word in string))
    