import pic
import func


def start():
    pic.root.bind('<Return>', func.displ(label_f, entry_f))
    pic.root.mainloop()


entry_f = pic.entry
label_f = pic.label
