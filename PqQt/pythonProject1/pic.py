from tkinter import *
from tkinter import ttk, Tk


def clear():
    entry.delete(0, END)


def display(event):
    label['text'] = entry.get()  # получаем введенный текст
    clear()


def bindings():
    root.bind('<Return>', display)


root = Tk()
root.title("Самопал Инк")
root.geometry("500x250")

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)



