

def enter():
    print('Хотите создать новую запись? ')
    new_1 = input('Если да то 1, если нет то 2: ')
    if new_1 != '1':
        print('Хотите редактировать запись? ')
        new_1 = input('Если да то 2, если нет то 3: ')
        if new_1 != '2':
            input('Хотите начать поиск? ')
            new_1 = input('Если да то 3, если нет, то 4 ')
            if new_1 != '3':
                print("К сожалению, выбранная Вами опция пока не разработана, зайдите попозже.")
                return -1
    return int(new_1)



def choose(new: int):
    if new == 1:
        famile_name = input('Введите фамилию: ')
        name = input('Введите имя: ')
        phone = input('Введите номер телефона: ')
        description = input('Добаьте описание: ')
        return f'{famile_name} {name} {phone} {description}'
    elif new == 2:
        print('Что будем редактировать?')
        print('Если хотите редактировать фамилию- введите 1, имя- введите 2, номер телефона - введите 3')
        edition = int(input('описание- введите 4: '))
        if edition == 1:
            old = input('Введите редактируемую фамилию: ')
            new = input('Введите новую фамилию: ')
        elif edition == 2:
            old = input('Введите редактируемое имя: ')
            new = input('Введите новое имя: ')
        elif edition == 3:
            old = input('Введите редактируемый номер телефона: ')
            new = input('Введите новый номер телефона: ')
        elif edition == 4:
            old = input('Введите старое описание: ')
            new = input('Введите старое описание: ')
        else:
            old = ''
            new = ''
        return f'{old} {new}'
    elif new == 3:
        search = input("Введите строку для поиска: ")
        return search










