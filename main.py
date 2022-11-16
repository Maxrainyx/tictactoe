def greet():
    print('''
            Приветствуем в игре
             Крестики-нолики!
---------------------------------------------------
        Формат ввода: x y
            x - номер строки (сверху вниз)
            у - номер столбца (слева на право)
---------------------------------------------------           
''')


c_game = True


def cont_game():
    ask = input('Введите "Да", чтобы повторить, или любой текст для выхода: ').lower()
    if ask != 'да':
        exit()

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask():
    while True:
        cords = input("         Ваш ход: ").split()
        
        if len(cords) != 2:
            print(" Введите только 2 координаты! ")
            continue
        
        x, y = cords
        
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue
        
        x, y = int(x), int(y)
        
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue
        
        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue
        
        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            cont_game()
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            cont_game()
            return True
    return False


while c_game:
    greet()
    field = [[" "] * 3 for i in range(3)]
    count = 0

    while True:
        count += 1
        show()
        if count % 2 == 1:
            print(" Ходит крестик!")
        else:
            print(" Ходит нолик!")

        x, y = ask()

        if count % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "0"

        if check_win():
            break

        if count == 9:
            print(" Ничья!")
            cont_game()
            break
