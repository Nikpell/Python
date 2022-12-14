from tkinter import *


def displ(smth1, smth2):
    def display(event):
        smth1['text'] = smth2.get()  # получаем введенный текст
        smth2.delete(0, END)

    display()
