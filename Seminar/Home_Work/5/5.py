import tkinter as tk

row = 3
column = 3
window = tk.Tk()

buttons = []
for i in range(row):
    temp = []
    for j in range(column):
        btn = tk.Button(window, width=3, font='Colibri 15 bold')
        temp.append(btn)
    buttons.append(temp)

for row_btn in buttons:
    print(row_btn)

for i in range(row):
    for j in range(column):
        btn = buttons[i][j]
        btn.grid(row=i, column=j)


window.mainloop()
