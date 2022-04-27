# ########## Викторина ########################################################################################№######
def game_victory():
    print('#'*100)
    print('           Игра ВИКТОРИНА')
    print('#'*100)
    year = input('Ввведите год рождения А.С.Пушкина:')
    while year != '1799':
        print('Не верно')
        year = input('Ввведите год рождения А.С.Пушкина: (подсказка 1799')

    day = input('Ввведите день рождения А.С.Пушкина?, в формате dd ')
    while day != '26':
        print('Не верно')
        day = input('В какой день мая родился Пушкин? 26? ')

    print('Верно\nGAME OVER')
    print('#'*100)

# ######## БАНКОВСКИЙ СЧЕТ ##########################################################################################

# ввод с клавиатуры положительного числа, при ошибке возвращает 0
def input_summa():
    summa = input('Укажите сумму: ')
    if summa.isdigit() and int(summa) > 0:
        summa = int(summa)
    else:
        summa = 0
    return summa


# увеличивает all_money на введенную сумму
def add_money(all_money = 0):
    print('\nВнесите деньги')
    summa = input_summa()
    all_money += int(summa)
    print(f'Вы внесли {summa} рублей, остаток {all_money}\n')
    return all_money


# увеличивает all_money на введенную сумму и также возвращает покупку
# tuple(сумма, наименование)
def spend_money(all_money):
    print('\nПокупка товара')
    summa = input_summa()

    if summa == 0:
        print('некорректная сумма\n')
        history_item = (0, '')
    elif all_money - summa < 0:
        print('не достаточно средств\n')
        history_item = (0, '')
    else:
        goods = input('Имя товара: ')
        print(f'Вы купили {goods} за {summa} рублей\n')
        history_item = (summa, goods)
        all_money -= summa
    return all_money, history_item


# печатает list с покупками
# одна строка = tuple(сумма, наименование)
def print_history(history):
    if len(history) == 0:
        print('\nУ Вас нет покупок\n')
    else:
        print('\nВаши покупки:')
        for i, stroke in enumerate(history):
            print(i + 1, stroke)
        print()


def game_bank():
    print('#'*100)
    print('           БАНКОВСКИЙ СЧЕТ')
    print('#'*100)
    cash = 0  # кошелек
    history = []  # история

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            cash = add_money(cash)

        elif choice == '2':
            cash, hist_item = spend_money(cash)
            if hist_item[0] > 0:
                history.append(hist_item)

        elif choice == '3':
            print_history(history)

        elif choice == '4':
            print('\nGAME OVER')
            print('#'*100)
            break
        else:
            print('Неверный пункт меню\n')
