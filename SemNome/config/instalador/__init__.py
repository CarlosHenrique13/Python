import os

if not os.path.exists('Armazena/Programas'):
    os.makedirs('Armazena/Programas')

def Instalardor():
    aplicativos_lista = os.listdir('Armazena/Programas')
    # fr"Armazena\Programas\{aplicativos_lista[0]}\{aplicativos_lista[0]}"
