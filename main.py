"""
1. Создать новый проект ""Консольный файловый менеджер"
2. В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- сохранить содержимое рабочей директории в файл
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- выход.
"""
import os
import sys
import shutil
import my_games

print("Консольный файловый менеджер")

while True:
    print('')
    print('1.  создать папку')
    print('2.  удалить (файл/папку)')
    print('3.  копировать (файл/папку)')
    print('4.  просмотр содержимого рабочей директории')
    print('5.  посмотреть только папки')
    print('6.  посмотреть только файлы')
    print('7.  просмотр информации об операционной системе')
    print('8.  создатель программы')
    print('9.  играть в викторину')
    print('10. мой банковский счет')
    print('11. сохранить содержимое рабочей директории в файл')
    print('12. ВЫХОД')

    choice = input('Выберите пункт меню: ')
    # ##################################################
    if choice == '1':
        print('\nСоздаем папку')
        obj_name = input('введите имя папки: ')
        if os.path.exists(obj_name):
            print('Папка уже существует')
        else:
            os.mkdir(obj_name)
            print(f'Папка {obj_name} создана')

    # ##################################################
    elif choice == '2':
        print('\nУдаляем файл/папку')
        obj_name = input('введите имя обьекта: ')
        if not os.path.exists(obj_name):
            print('Обьект не существует')
        else:
            if os.path.isdir(obj_name):
                os.rmdir(obj_name)
                print(f'Папка {obj_name} удалена')
            else:
                os.remove(obj_name)
                print(f'Файл {obj_name} удален')

    # ##################################################
    elif choice == '3':
        print('\nКопируем файл/папку')
        obj_name = input('введите имя обьекта: ')
        if not os.path.exists(obj_name):
            print('Обьект не существует')
        else:
            shutil.copy(obj_name,'copy_'+obj_name)
            print(f'Обьект {obj_name} скопирован')

    # ##################################################
    elif choice == '4':
        print('\nПросмотр содержимого рабочей директории:')
        print(os.listdir())

    # ##################################################
    elif choice == '5':
        print('\nПросмотр содержимого рабочей директории/ТОЛЬКО ПАПКИ:')
        all_names = os.listdir()
        for obj_name in all_names:
            if os.path.isdir(obj_name):
                print(obj_name)

    # ##################################################
    elif choice == '6':
        print('\nПросмотр содержимого рабочей директории/ТОЛЬКО ФАЙЛЫ:')
        all_names = os.listdir()
        for obj_name in all_names:
            if os.path.isfile(obj_name):
                print(obj_name)

    # ##################################################
    elif choice == '7':
        print('\nОперционная система:')
        print(sys.platform)

    # ##################################################
    elif choice == '8':
        print('\nПрограмма создана:')
        print('Создатель Креатив Иванович, 2022')

    # ##################################################
    elif choice == '9':
        print('\nИграем в Викторину:')
        my_games.game_victory()

    # ##################################################
    elif choice == '10':
        print('\nМой банковский счет:')
        my_games.game_bank()

    # ##################################################
    elif choice == '11':
        print('\nСохранение содержимого рабочей директории в файл listdir.txt')
        names_file = 'files:'
        names_dir = 'dirs:'

        all_names = os.listdir()
        for obj_name in all_names:
            if os.path.isfile(obj_name):
                names_file += ' ' + str(obj_name) + ','
            elif os.path.isdir(obj_name):
                names_dir += ' ' + str(obj_name) + ','

        names_file = names_file[:-1]  # запятая в конце не нужна
        names_dir = names_dir[:-1]

        with open('listdir.txt', 'w') as f:
            f.write(names_file)
            f.write('\n')
            f.write(names_dir)

        print('\nСохранено успешно')

    # ##################################################
    elif choice == '12':
        print('\nКонсольный файловый менеджер завершил работу')
        break

    else:
        print('Неверный пункт меню\n')