import data_base as db

string = ''


def show_click(event):
    global string
    string = ''.join(db.show_contact()).replace(';', '  ')
    print(string)


def load_click(event):
    print('нажата кнопка Загрузитьь')


def save_click(event):
    print('нажата кнопка Сохранить')


def add_click(event):
    print('нажата кнопка Добаваить')


def change_click(event):
    print('нажата кнопка Изменить')


def del_click(event):
    print('нажата кнопка Удалить')


def search_click(event):
    print('нажата кнопка Поиск')


def exit_click(event):
    print('нажата кнопка Выход')


def set_text():
    global string
    return string


def get_phone_book(book_list):
    return None