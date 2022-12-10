table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # поле 3х3
ship = table[1][1]


#

def prepare_table():
    table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in table:
        print(table)
    print()
    table[1][1] = 0  # расположение корабля,присваиваю значение 0,для наглядности


def show_map():
    for i in table:
        print(i)
    print()


# print(ship)


# shot_x = int(input('Введите координаты выстрела X (от 0 до 2) : '))
# shot_y = int(input('Введите координаты выстрела Y( от 0 до 2) : '))
# miss1 = table[0][0]  # здесь прописанно молоко,оно в последующем мне не пригодилось
# miss2 = table[0][1]
# miss3 = table[0][2]
# miss4 = table[1][0]
# miss5 = table[1][2]
# miss6 = table[2][0]
# miss7 = table[2][1]
# miss8 = table[2][2]
# shot1 = table[shot_x][shot_y]
def game():
    while True:

        shot_x = int(input('Введите координаты выстрела X (от 0 до 2) : '))
        shot_y = int(input('Введите координаты выстрела Y( от 0 до 2) : '))
        shot1 = table[shot_x][shot_y]
        if shot1 == ship:
            print('Убил')
            break
        else:
            print('MIMO')
            continue


# немного черновая работа, но моя победа в том,что я разобрался как выходить из цикла и продолжить его с начала =)
# крестики нолики могу отправить потом,если потребуется для нормальной оценки(хочется спать)
prepare_table()
show_map()
game()
