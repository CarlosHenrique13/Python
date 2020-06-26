from tkinter import *
import os


#Criar novo Usuario
def NewUser(user,senha):
    arg = open("Proprietes/Usuario.user","at")
    arg.write(f"Usuario={user}\n")
    arg.write(f"Passowrd={senha}\n")
    arg.close()


#Verificar se o usuario Existe
def UserPermiter(user,senha):
    arg = open("Proprietes/Usuario.user",'rt')
    linhas = arg.readlines()
    linha = []
    for l in range(0,len(linhas)):
        linha.append(linhas[l][:len(linhas[l])-1].split())
    print(linha)
    return False

#Confirma o Usuario se Existe
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
    a = UserPermiter(nome,senha)
    if a:
        return True
    userconf.mainloop()



    