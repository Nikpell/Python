def get_phone_book(book_list):
    phone_book = book_list
    if len(phone_book) < 1:
        return 'Телефонная книга пуста'
    else:
        book_string = ''
        for id, contact in enumerate(phone_book, 1):
            book_string += f"{id}  {contact.replace(';', '  ')}"
    return book_string


def search_in_phone_book(string, phone_book):
    search_string = ''
    for id, contact in enumerate(phone_book, 1):
        if contact.count(string):
            search_string += f"{id}  {contact.replace(';', '  ')}"
    if search_string == '':
        return f'Не могу найти запись, содержащую {string}'
    return search_string


def search_contact(string, phone_book):
    index = int(string)
    return phone_book[index - 1].replace(';', '  ')


def verify_contact(string, phone_book):
    flag = False
    try:
        index = int(string)
        if -1 < index - 1 < len(phone_book):
            return flag
        else:
            return True
    except:
        return True


def verify_change_what(string):
    flag = False
    try:
        index = int(string)
        if -1 < index < 4:
            return flag
        else:
            return True
    except:
        return True


def change_contact(new_string, contact_string, position_string, phone_book):
    new_contact = phone_book[int(contact_string) - 1].split(';')
    new_contact[int(position_string) - 1] = new_string
    phone_book[int(contact_string) - 1] = ';'.join(new_contact)
    return phone_book

def delete_contact(contact):
    if contact == '1':
        return True
    else:
        return False


