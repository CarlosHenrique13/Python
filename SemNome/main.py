from tkinter.messagebox import showinfo
from config.conf import *
from complet import *
from config.instalador import *

#Para Verificar Quando Iniciar o Aplicativo
def Inicializar():
    Instalardor()
    conf = ConfigAnalise()
    if conf == False:
        Interface()

Inicializar()