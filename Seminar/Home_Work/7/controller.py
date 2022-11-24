import gui
import choose
import Database


def start():
    result_enter = gui.enter()  # получает щапись, редактирование
    result_choose = gui.choose(result_enter)  # получает строку в результате выбора
    data_get = Database.get_info()  # получает данные из бвзы
    data_set = choose.new_data(result_choose, result_enter, data_get) # добавление, перезапись , замена
    Database.save_info(data_set) # перезаписывает новый файл






