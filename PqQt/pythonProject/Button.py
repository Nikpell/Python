from tkinter import *
from tkinter import ttk

clicks = 0


def click_button():
    global clicks
    clicks += 1
    btn['text'] = f'Clicks {clicks}'


root = Tk()
root.title('Hello Button')
root.geometry('200x200')

btn = ttk.Button(text='Click me', command=click_button)
btn.pack()

# btn = ttk.Button(text="Click Me", state=["disabled"]) state=["disabled"] делает кнопку неактивной
root.mainloop()

# command: функция, которая вызывается при нажатии на кнопку
#
# compund: устанавливает расположение картинки и текста относительно друг друга
#
# cursor: курсор указателя мыши при наведении на метку
#
# image: ссылка на изображение, которое отображается на метке
#
# pading: отступы от границ вилжета до его текста
#
# state: состояние кнопки
#
# text: устанавливает текст метки
#
# textvariable: устанавливает привязку к элементу StringVar
#
# underline: указывает на номер символа в тексте кнопки, который подчеркивается. По умолчанию значение -1, то есть никакой символ не подчеркивается
#
# width: ширина виджета
