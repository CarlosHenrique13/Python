from tkinter.messagebox import showinfo
from config.conf import *
from complet import *


#Para Verificar Quando Iniciar o Aplicativo
def Inicializar():
    conf = ConfigAnalise()
    if conf == False:
        Interface()

Inicializar()