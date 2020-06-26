from tkinter import *
from config.conf import *
#from config.user import *
from complet import*
import os

#Para Verificar Quando Iniciar o Aplicativo
def Inicializar():
    conf = ConfigAnalise(raiz=os.getcwdb)
    

Inicializar()

#Criação da Janela
janela = Tk()
janela.title("Projeto Nome")
janela.geometry("500x400")

janela.mainloop()
