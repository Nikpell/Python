from tkinter import *


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print('Закрытие приложения')


root = Tk()
root.geometry('300x200')

root.title('Привет мир')
root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()
