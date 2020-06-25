from tkinter import *

#Confima o Usuario se Existe
def UesrConfirme():
    userconf = Tk()
    userconf.title("Login")
    userconf.geometry("100x200")
    Label(userconf,text="Usuario:").place(x=5,y=5)
    nome = Entry()
    nome.place(x=80,y=5)
    senha = Entry("*")
    senha.place(x=5,y=50)
    if senha == "1":
        return True
    userconf.mainloop()
    