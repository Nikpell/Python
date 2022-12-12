# Метод grid применяет следующие параметры:
#
# column: номер столбца, отсчет начинается с нуля
#
# row: номер строки, отсчет начинается с нуля
#
# columnspan: сколько столбцов должен занимать элемент
#
# rowspan: сколько строк должен занимать элемент
#
# ipadx и ipady: отступы по горизонтали и вертикали соответственно от границ элемента до его содержимого
#
# padx и pady: отступы по горизонтали и вертикали соответственно от границ ячейки грида до границ элемента
#
# sticky: выравнивание элемента в ячейке, если ячейка больше элемента.
# Может принимать значения n, e, s, w, ne, nw, se, sw, которые указывают соответствующее направление выравнивания

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello word")
root.geometry('500x500')

for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=1)

for r in range(3):
    for c in range(3):
        btn = ttk.Button(text=f"({r},{c})")
        btn.grid(row=r, column=c)

root.mainloop()