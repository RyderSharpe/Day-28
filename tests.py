from tkinter import *

app = Tk()

# Text Widget + Font Size
txt = Text(app, font=('Verdana',8))
txt.pack()

# Delete Button
btn = Button(app, text='Delete', command=lambda: txt.delete(1.0,END))
btn.pack()

app.mainloop()