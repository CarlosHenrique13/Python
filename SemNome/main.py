from tkinter.messagebox import showinfo
from tkinter import *
from config.conf import *
from complet import*
import os

showinfo(title='Enfore', message='Não á (.txt)')

#Para Verificar Quando Iniciar o Aplicativo
def Inicializar():
    conf = ConfigAnalise()
    print(conf)
    

#Inicializar()
def Interface():
    #Criação da Janela
    janela = Tk()
    janela.title("Projeto Nome")
    janela.geometry("500x400")
    janela.mainloop()

