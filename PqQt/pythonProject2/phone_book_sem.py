import view_sem

phone_book = []

def get_phone_book():
    global phone_book
    print(f'get_phone_book = {phone_book}')
    return phone_book

def set_phone_book(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book
    # print(f'set phone_book = {phone_book}, {new_phone_book}')

def add_contact():
    global phone_book
    contact = view.input_new_contact()
    phone_book.append(contact)

def remove_contact():
    global phone_book
    id = view.input_remove_contact()
    confirm = input(f'Вы точно хотите удалить контакт f{phone_book[id - 1][0]}? (y/n)')
    if confirm.lower() == 'y':
        del_contact = phone_book.pop(id - 1)

