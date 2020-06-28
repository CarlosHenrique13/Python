from tkinter.messagebox import showinfo
from tkinter import *
from config.conf import *
from complet import *
import os


#Para Verificar Quando Iniciar o Aplicativo
def Inicializar():
    conf = ConfigAnalise()
    if conf == False:
        Interface()

Inicializar()