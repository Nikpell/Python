import tkinter as tk
import functions as fun
import data_base as db


def picture():
    # Создается новое окно с заголовком "Телефонная книга".
    window = tk.Tk()
    window.title("Телефонная книга")


    # Создается новая рамка `frm_form` для ярлыков с текстом и
    # Однострочных полей для ввода информации об адресе.
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    # Помещает рамку на окно приложения.
    frm_form.pack()

    # Список ярлыков полей.
    labels = [
        "Имя:",
        "Телефон:",
        "Коментарий:",
    ]

    # Цикл для списка ярлыков полей.
    for idx, text in enumerate(labels):
        # Создает ярлык с текстом из списка ярлыков.
        label = tk.Label(master=frm_form, text=text)
        # Создает текстовое поле которая соответствует ярлыку.
        entry = tk.Entry(master=frm_form, width=50)
        # Использует менеджер геометрии grid для размещения ярлыков и
        # текстовых полей в строку, чей индекс равен idx.
        label.grid(row=idx, column=0, sticky="e")
        entry.grid(row=idx, column=1)

    # Создает новую рамку `frm_buttons` для размещения в ней
    # кнопок. Данная рамка заполняет
    # все окно в горизонтальном направлении с
    # отступами в 5 пикселей горизонтально и вертикально.
    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    # Создает новую рамку `txt_buttons` для размещения в ней окна всех записей
    frm_txt = tk.Frame()
    frm_txt.pack(fill=tk.X, ipadx=5, ipady=5)

    # Создает кнопки и размещает их
    # внутри рамки `frm_buttons`.
    btn_show = tk.Button(master=frm_buttons, text="Показать телефонную книгу ", command=fun.show_click())
    btn_show.grid(row=0, column=0, sticky="nsew")

    btn_load = tk.Button(master=frm_buttons, text="Загрузить телефонную книгу")
    btn_load.grid(row=0, column=1, sticky="nsew")

    btn_save = tk.Button(master=frm_buttons, text="Сохранить телефонную книгу")
    btn_save.grid(row=1, column=0, sticky="nsew")

    btn_add = tk.Button(master=frm_buttons, text="Добавить контакт")
    btn_add.grid(row=1, column=1, sticky="nsew")

    btn_change = tk.Button(master=frm_buttons, text="Изменить контакт")
    btn_change.grid(row=2, column=0, sticky="nsew")

    btn_del = tk.Button(master=frm_buttons, text="Удалить контакт")
    btn_del.grid(row=2, column=1, sticky="nsew")

    btn_search = tk.Button(master=frm_buttons, text="Найти контакт")
    btn_search.grid(row=3, column=0, sticky="nsew")

    btn_exit = tk.Button(master=frm_buttons, text="Выйти из приложения")
    btn_exit.grid(row=3, column=1, sticky="nsew")

    # Создает окно вывода и размещает его
    # внутри рамки `frm_txt`.

    txt_show = tk.Label(master=frm_txt)
    txt_show.grid(row=0, column=0, sticky="nsew")

    # обработчик событий
    # btn_show.bind("<Button-1>", fun.show_click)
    btn_load.bind("<Button-1>", fun.load_click)
    btn_save.bind("<Button-1>", fun.save_click)
    btn_add.bind("<Button-1>", fun.add_click)
    btn_change.bind("<Button-1>", fun.change_click)
    btn_del.bind("<Button-1>", fun.del_click)
    btn_search.bind("<Button-1>", fun.search_click)
    btn_exit.bind("<Button-1>", fun.exit_click)

    # Запуск приложения.
    window.mainloop()
