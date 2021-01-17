import Copyfile as cp
import random
import Findlast as fl

cp.create_result_file()

removing_str = []

class Cases:
    global final_len_list #не понимаю почему эта переменная не распостраняется на следующую функцию
    def __init__(self, final_len_list=11):
        self.final_len_list = final_len_list
        print(final_len_list)

    def remove_str(self):
        """Суть функции чтобы удалить случайный элемент из списка 'qwerty', дублирующего исходный файл"""
        for a in range(len(qwerty) - final_len_list):
            qwerty.pop(random.randint(1, len(qwerty)))
        return print(len(qwerty))


print(len(fl.full_file))
print(fl.full_file)

qwerty = fl.full_file #дублировал в список, так как эта штука станет классом

otvet = input('Хотите выбрать число строк? ')

if otvet == 'Да':
    fl.full_file = Cases(int(input('Сколько строк необходимо? ')))
else:
    fl.full_file = Cases()

fl.full_file.remove_str()

print(qwerty)