import view
import date_base as db
import function as func


def choice_menu(choice):
    match choice:
        case 1:
            book_list = db.from_date_base()
            book_string = func.get_phone_book(book_list)
            view.print_phone_book(book_string)
        case 2:
            view.error()
        case 3:
            view.error()
        case 4:
            new_contact = view.input_new_contact()
            db.to_date_base(new_contact)
        case 5:
            contact_string = view.change_contact()
            phone_book = db.from_date_base()
            while func.verify_contact(contact_string, phone_book):
                view.print_phone_book('Вы ввели неверный номер. Внимательнее пожалуйста')
                contact_string = view.change_contact()
            position_string = view.change_what(func.search_contact(contact_string, phone_book))
            while func.verify_change_what(position_string):
                position_string = view.change_what('Вы ввели неверный номер. Внимательнее пожалуйста')
            new_date = view.changing()
            phone_book = func.change_contact(new_date, contact_string, position_string, phone_book)
            db.change_phone_book(phone_book)
        case 6:
            phone_book = db.from_date_base()
            contact = view.delete_contact()
            while func.verify_contact(contact, phone_book):
                contact = view.change_contact()
            verify = view.verify_delete_contact(contact)
            if func.delete_contact(verify):
                phone_book.pop(int(contact) - 1)
                db.change_phone_book(phone_book)
        case 7:
            string_for_search = view.search_contact()
            phone_book = db.from_date_base()
            view.print_phone_book(func.search_in_phone_book(string_for_search, phone_book))
        case 0:
            return True


def start():
    while True:
        choice = view.main_menu()
        if choice_menu(choice):
            break
