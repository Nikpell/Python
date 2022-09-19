#
# Создайте программу для игры в ""Крестики-нолики"".
# Своя попытка
# TODO попытаться добить

import tkinter as tk


class MyButton(tk.Button):
    def __init__(self, master, x, y, number, *args, **kwargs ):
        super(MyButton, self).__init__(master, width=3, font='Colibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False

    def __repr__(self):
        return f'MyButton {self.x} {self.y}, {self.number}'

class CrossAndZero:
    window = tk.Tk()
    ROW = 3
    COLUMN = 3

    def __init__(self):
        self.buttons = []
        counter = 1
        for i in range(CrossAndZero.ROW):
            temp = []
            for j in range(CrossAndZero.COLUMN):
                btn = MyButton(CrossAndZero.window, x=i, y=j, number=counter)
                btn.config(command=lambda button=btn: self.click(button))
                temp.append(btn)
                counter += 1
            self.buttons.append(temp)

    def click(self, clicked_button: MyButton):
        print(clicked_button)



    def create_widgets(self):
        for i in range(CrossAndZero.ROW):
            for j in range(CrossAndZero.COLUMN):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def start(self):
        self.create_widgets()
        self.print_buttons()
        print(self.get_places())
        CrossAndZero.window.mainloop()

    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)

    # def insert_places(self):
    #     for row_btn in self.buttons:
    #         for btn in row_btn:



    def get_places(self):
        indexes = []
        for i in range(self.ROW):
            temp = []
            for j in range(self.COLUMN):
                temp.append(self.ROW + 1)
            indexes.append(temp)
        return indexes

game = CrossAndZero()
game.start()
