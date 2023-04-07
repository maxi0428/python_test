from tkinter import *
window = Tk()

photo = PhotoImage(file = "gif/dog13.gif")
photo2 = PhotoImage(file = "gif/dog12.gif")
photo3 = PhotoImage(file = "gif/dog11.gif")
photo4 = PhotoImage(file = "gif/dog10.gif")
label1 = Label(window, image = photo)
label2 = Label(window, image = photo2)
label3 = Label(window, image = photo3)
label4 = Label(window, image = photo4)

label1.pack(side=LEFT)
label2.pack(side=RIGHT)
label3.pack(side=TOP)
label4.pack(side=BOTTOM)

window.mainloop()
