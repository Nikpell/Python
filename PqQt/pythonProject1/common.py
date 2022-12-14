from tkinter import *
from tkinter import ttk, Tk


def clear():
    entry.delete(0, END)


def display(event):
    summa = 0
    string = entry.get()  # получаем введенный текст
    clear()
    if string[-1] != '=':
        label_1['text'] += f'{string} '
    else:
        label_1['text'] += f'{string} '
        summa = eval(label_1['text'][0:-2])
        label_1['text'] += f'{int(summa)}'
        entry(state=DISABLED)


def bindings():
    root.bind('<Return>', display)


root = Tk()
root.title("Самопал Инк")
root.geometry("500x250")

label_1 = ttk.Label()
label_1.pack(anchor=NW, padx=6, pady=6)

label_2 = ttk.Label()
label_2.pack(anchor=NW, padx=6, pady=6)

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)

bindings()

root.mainloop()
