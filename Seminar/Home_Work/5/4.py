# сапер изучение tkinter и ООП
import tkinter as tk
from random import shuffle

colors = {
    0: 'white',
    1: '#0320fc',  # online color picker
    2: '#03fc62',
    3: '#f4fc03',
    4: '#fc03d3',
    5: '#fc2803',
    6: '#fc0345',
    7: '#d92323',
    8: '#7a0505'

}


class MyButton(tk.Button):
    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Colibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
        self.count_bomb = 0
        self.is_open = False

    def __repr__(self):
        return f'MyButton {self.x} , {self.y}, {self.number}, {self.is_mine}'


class MineSweeper:
    rows = 10
    columns = 10
    window = tk.Tk()
    mines = 10

    def __init__(self):
        self.buttons = []
        # создание кнопок
        for i in range(MineSweeper.rows +2):
            temp = []
            for j in range(MineSweeper.columns + 2):
                btn = MyButton(MineSweeper.window, x=i, y=j)
                btn.config(command=lambda button=btn: self.click(button))
                temp.append(btn)
            self.buttons.append(temp)

    def click(self, clicked_button: MyButton):
        print(clicked_button)
        if clicked_button.is_mine:
            clicked_button.config(text='*', background='red', disabledforeground='black')
            clicked_button.is_open = True
        else:
            color = colors.get(clicked_button.count_bomb, 'black')
            if clicked_button.count_bomb:
                clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
                clicked_button.is_open = True
            else:
                self.breadth_first_search(clicked_button)
        clicked_button.config(state='disabled')
        clicked_button.config(relief=tk.SUNKEN)

    def breadth_first_search(self, btn: MyButton):
        queue = [btn]
        while queue:

            cur_btn = queue.pop()
            color = colors.get(cur_btn.count_bomb, 'black')
            if cur_btn.count_bomb:
                cur_btn.config(text=cur_btn.count_bomb, disabledforeground=color)
            else:
                cur_btn.config(text='', disabledforeground=color)
            cur_btn.is_open = True
            cur_btn.config(state='disabled')
            cur_btn.config(relief=tk.SUNKEN)
            x = cur_btn.x
            y = cur_btn.y  #обход в ширину
            if cur_btn.count_bomb == 0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if abs(dx - dy) != 1:
                            continue
                        nex_btn = self.buttons[x + dx][y + dy]
                        if not nex_btn.is_open and 1 < nex_btn.x <= MineSweeper.rows \
                                and 1 < nex_btn.y <= MineSweeper.columns and nex_btn not in queue:
                            queue.append(nex_btn)

    def create_widgets(self):
        for i in range(1, MineSweeper.rows + 1):
            for j in range(1, MineSweeper.columns + 1):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def open_all_button(self):
        for i in range(MineSweeper.rows +2):
            for j in range(MineSweeper.columns +2):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    btn.config(text='*', background='red', disabledforeground='black')
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, 'black')
                    btn.config(text=btn.count_bomb, fg=color)



    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.counts_mines_in_buttons()
        self.print_button()
        # self.open_all_button()
        MineSweeper.window.mainloop()

    def print_button(self):
        for i in range(1, MineSweeper.rows + 1):
            for j in range(1, MineSweeper.columns + 1):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    print('B', end='')
                else:
                    print(btn.count_bomb, end='')
            print()

    def insert_mines(self):
        index_mines = self.get_mines_places()
        print(index_mines)
        counter = 1
        for i in range(1, MineSweeper.rows + 1):
            for j in range(1, MineSweeper.columns + 1):
                btn = self.buttons[i][j]
                btn.number = counter
                if btn.number in index_mines:
                    btn.is_mine = True
                counter += 1

    def counts_mines_in_buttons(self):
        for i in range(1, MineSweeper.rows + 1):
            for j in range(1, MineSweeper.columns + 1):
                btn = self.buttons[i][j]
                count_bomb = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbor = self.buttons[i + row_dx][j + col_dx]
                            if neighbor.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb


    @staticmethod
    def get_mines_places():
        indexes = list(range(1, MineSweeper.columns * MineSweeper.rows + 1))
        shuffle(indexes)
        return indexes[:MineSweeper.mines]


game = MineSweeper()
game.start()
