def main_menu():
    print('Выберете команду меню: \n1. Показать телефонную книгу\n2. Загрузить телефонную книгу\n'
          '3. Сохранить телефонную книгу\n4. Добавить контакт\n5. Изменить контакт\n6. Удалить контакт'
          '\n7. Найти контакт\n0. Выйти из приложения')
    return input_menu()


def input_menu():
    while True:
        try:
            choice = int(input('Введите пункт меню: '))
            if choice in range(0, 8):
                return choice
            else:
                print('Такого пункта меню нет. Внимательнее пожалуйста')
        except:
            print('Ошибка ввода. Введите корректный пункт меню.')


def print_phone_book(book_string):
    print()
    print(book_string)
    print()


def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий контакта: ')
    new_contact = [name, phone, comment]
    return new_contact


def search_contact():
    string = input('Введите часть имени, телефона, или комментария, который будем искать: ')
    return string


def change_contact():
    string = input('Введите номер контакта, в котором что то хотите поменять, '
                   'если не знаете\n то воспользуйтесь поиском контакта, '
                   'для этого введите 1 и при следующем запросе 0: ') # Выход корявенький, придумать оптимальнее
    return string

def change_what(string):
    print(string)
    print('Если хотите изменить Имя введите 1')
    print('Если хотите изменить Телефон введите 2')
    print('Если хотите изменить Комментарий введите 3')
    print('Если ничего не хотите менять введите 0')
    string = input('Ожидаю вариант: ')
    return string

def changing():
    new_date = input('Введите новый вариант: ')
    return new_date

def input_remove_contact():
    print()
    print_phone_book()
    id = int(input('Введите iD контакта, который хотите удалить: '))
    return id


def error():
    print('Пардону просим, такой функции пока нет, будет ли, пока не известно')
    print()

def delete_contact():
    string = input('Введите номер контакта, который хотите удалить, '
                   'если не знаете номер\n то воспользуйтесь поиском контакта, '
                   'для этого введите 1 и при следующем запросе 0: ') # Выход корявенький, придумать оптимальнее
    return string

def verify_delete_contact(contact):
    verify = input(f'Вы хотите удалить контакт {contact}. Уверены? 1- да, 0- нет: ')
    return verify
