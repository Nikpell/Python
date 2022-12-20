import data_base_sem
import view_sem
import phone_book_sem as pb


def choice_menu(choice):
    match choice:
        case 1:
            view.print_phone_book()
        case 2:
            data_base.load_contact()
        case 3:
            data_base.save_contact()
        case 4:
            pb.add_contact()
        case 5:
            pass
        case 6:
            pb.remove_contact()
        case 7:
            pass
        case 0:
            return True



while True:
    choice = view.main_menu()
    if choice_menu(choice):
        break
