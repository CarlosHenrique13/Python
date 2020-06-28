from tkinter.messagebox import showinfo
from tkinter import *
from complet import *
import os


#Criar novo Usuario
def NewUser(user,senha):
    arg = open("Proprietes/Usuario.user","at")
    arg.write(f"Usuario={user}\n")
    arg.write(f"Passowrd={senha}\n")
    arg.close()


#Verificar se o usuario Existe
def UserPermiter(janela,user,senha):
    arg = open("Proprietes/Usuario.user",'rt')
    linhas = arg.readlines()
    linha = []
    inf = False
    for l in range(0,len(linhas)):
        linha.append(linhas[l][:len(linhas[l])-1].split("="))
    for log in range(1,len(linha)):
        for i in range(len(linha[log])):
            try:
                if (linha[log][i] == user) and (linha[log+1][i] == senha):
                   janela.destroy()
                   inf = Interface()
            except:
                pass
    if inf == True:
        exit()
    else:
        janela.destroy()
        showinfo(title='Login', message='Usuario ou senha Incorreta.')
        exit()

#Confirma o Usuario se Existe
def UesrConfirme():
    userconf = Tk()
    userconf.title("Login")
    userconf.geometry("250x100")
    Label(userconf,text="Usuario:").place(x=5,y=5)
    nome = Entry(userconf)
    nome.place(x=55,y=5)
    Label(userconf,text="Senha:").place(x=5,y=30)
    senha = Entry(userconf,show="*")
    senha.place(x=50,y=30)
    libera = Button(userconf,text="Confirma",command=lambda: UserPermiter(userconf,nome.get(),senha.get()))
    libera.place(x=125,y=60)
    userconf.mainloop()

    