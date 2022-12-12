from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Hello world')
root.geometry('300x300')

# btn = ttk.Button(text='Click')
btn = ttk.Button()
btn.pack()

btn.config(text='Send')

root.mainloop()

# Button: кнопка
#
# Label: текстовая метка
#
# Entry: однострочное текстовое поле
#
# Text: многострочное текстовое поле
#
# Checkbutton: флажок
#
# Radiobutton: переключатель или радиокнопка
#
# Frame: фрейм, который организует виджеты в группы
#
# Listbox: список
#
# Combobox: выпадающий список
#
# Menu: элемент меню
#
# Scrollbar: полоса прокрутки
#
# Treeview: позволяет создавать древовидные и табличные элементы
#
# Scale: текстовая метка
#
# Spinbox: список значений со стрелками для перемещения по элементам
#
# Progressbar: текстовая метка
#
# Canvas: текстовая метка
#
# Notebook: панель вкладок