from tkinter import *
import os

#Confima o Usuario se Existe
def UesrConfirme():
    userconf = Tk()
    userconf.title("Login")
    userconf.geometry("250x100")
    Label(userconf,text="Usuario:").place(x=5,y=5)
    nome = Entry()
    nome.place(x=55,y=5)
    Label(userconf,text="Senha:").place(x=5,y=30)
    senha = Entry(show="*")
    senha.place(x=50,y=30)
    envia = Button(userconf,text="Confirma")
    envia.place(x=125,y=60)
    if senha == "1":
        return True
    userconf.mainloop()

#Criar novo Usuario
def NewUser(user,senha):
    arg = open("Proprietes\Usuario.user","at")
    arg.write(f"Usuario={user}\n")
    arg.write(f"Passowrd={senha}\n")
    arg.close()

    