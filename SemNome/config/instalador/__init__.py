import os
from tkinter import *




#Para Criação de Apps
class Instal():
    def __init__(self,janela):
        self.janela = janela
        local = os.getcwd()
        print(local)

    def interface(self,objeto,x=0,y=0):
        item = objeto
        item.place(x=x,y=y)
        self.janela.update()



#
def InstalardorInic(janela):
    Label(janela,text="oi").place(x=0,y=0)
    tela = Instal(janela)
    tela.interface(Entry(janela))
    arg = open("Janela.txt","wt+")
    arg.write(f"{janela}\n")
    arg.close()
#Inicialização dos app
def IniciApps():
    pass
