#–еализовать функцию int_func(), принимающую слово из маленьких латинских 
#букв и возвращающую его же, но с прописной первой буквой. Ќапример, 
#print(int_func(СtextТ)) -> Text

def up_letter(s):
    return s.capitalize()
string = input('¬ведите строку из слов дл€ обработки: ').split()
print(' '.join(up_letter(word) for word in string))
    