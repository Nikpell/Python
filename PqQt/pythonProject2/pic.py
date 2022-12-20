from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Самопал инк.')
root.geometry('1000x600')

label_title = ttk.Label(text='Записная книжка', font=('Arial', 16))
label_title.pack()

label_name = ttk.Label(root, text='Имя')
label_name.place(x=100, y=50)
label_phone = ttk.Label(root, text='Телефон')
label_phone.place(x=400, y=50)
label_comment = ttk.Label(root, text='Комментарий')
label_comment.place(x=700, y=50)

name = ttk.Entry()
name.place(x=10, y=70)
phone = ttk.Entry()
phone.place(x=330, y=70)
comment = ttk.Entry()
comment.place(x=650, y=70)


root.mainloop()