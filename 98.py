
# create a gui to taje data from user and store it to txt file



import tkinter
top = tkinter.Tk()
file =  open("user_gui.txt","a+")

# Code to add widgets will go here...
def save():
    global file
    file.close()
    file =  open("user_gui.txt","a+")
def close():
    file.close()
    top.destroy()
def add():
    file.write(user_value.get()+'\n')
    E1.delete(0,'end')


user_value = tkinter.StringVar()

E1 = tkinter.Entry(top, bd =5,textvariable=user_value)
E1.pack(side = 'right')
button_add = tkinter.Button(top, text="Add line", command=add)
button_add.pack()
B = tkinter.Button(top, text ="SAVE",command=save)
B.pack(side = 'bottom')
A= tkinter.Button(top, text ="SAVE and CLOSE",command=close)
A.pack(side = 'bottom')

# A.pack()
# B.pack()
top.mainloop()
