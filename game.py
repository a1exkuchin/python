# -*- coding: utf-8 -*-
import random
class Player:
    @property
    def gen_card(self):
        random.seed()
        values = [sorted(random.sample(list(range((8 - j) // 8 + 10 * j, 10 * (j + 1) + j // 8)), 3)) for j in range(9)]
        card_values = list()
        for i in range(3):
            del_index = random.sample(list(range(9)),4)
            for j in range(9):
                if j in del_index:
                    card_values.append(0)
                else:
                    card_values.append(values[j][i])
        return card_values
    def card_text(self, values):
        text = ''
        for i in range(3):
            row = ''
            for j in range(9):
                if values[i * 9 + j] == 0:
                    row += ' '*3
                elif values[i * 9 + j] == -1:
                    row += '  -'
                else:
                    row +='{:3d}'.format(values[i * 9 + j])
            text += row + '\n'
        return text[:-1]    

user = Player()
computer = Player()

card_user = user.gen_card
card_computer = computer.gen_card
bag = random.sample(list(range(1, 91)), 90)

while len(bag) > 0:
    keg = bag.pop()
    print(f'Новый бочонок: {keg} (осталось {len(bag)})')
    print('------ Ваша карточка ------')
    print(user.card_text(card_user))
    print('---------------------------')
    print('--- Карточка компьютера ---')
    print(computer.card_text(card_computer))
    print('---------------------------')
    if sum(card_user) == -15:
        print('Вы выиграли')
        break
    if sum(card_computer) == -15:
        print('Вы проиграли')
        break
    inp_text = input('Зачеркнуть цифру? (y/n) ')
    if keg in card_computer:
        card_computer[card_computer.index(keg)] = -1 
    if inp_text =='y' and keg in card_user:
        card_user[card_user.index(keg)] = -1 
        continue
    elif inp_text !='y' and not(keg in card_user):
        continue
    else:
        print('Вы проиграли')
        break
     
    