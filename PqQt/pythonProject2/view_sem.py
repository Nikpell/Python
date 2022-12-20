import phone_book_sem as pb
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

def print_phone_book():
    phone_book = pb.get_phone_book()
    print()
    if len(phone_book) < 1:
        print('Телефонная книга пуста или не загружена')
    else:
        for id, contact in enumerate(phone_book, 1):
            print(id, contact)
    print()

def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий контакта: ')
    new_contact = [name, phone, comment]
    return new_contact

def input_remove_contact():
    print()
    print_phone_book()
    id = int(input('Введите iD контакта, которыйхотите удалить: '))
    return id

