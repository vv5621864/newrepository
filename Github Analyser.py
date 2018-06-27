from tkinter import *



def login():
    un=E1.get()
    pa=E2.get()
    
    

top=Tk()

top.geometry("1600x1600")
top.configure(background='green')

L1=Label(top,text='User Name')
L1.grid(row=0, column=0)
##L1.pack(side=LEFT)
E1=Entry(top,bd=5)
E1.grid(row=0, column=1)
##E1.pack(side=RIGHT)


L2=Label(top,text='Password')
L2.grid(row=1, column=0)
##L1.pack(side=RIGHT)
E2=Entry(top,show='*',bd=5)
E2.grid(row=1, column=1)
##E1.pack(side=RIGHT)

b1=Button(top,text='Login',bg='blue',command=login)
b1.grid(row=2, column=1)
##b1.pack(side=LEFT)

top.mainloop()
