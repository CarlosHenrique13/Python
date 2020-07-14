#Locais
from func import *
from classes import *

#Externas
import os
from tkinter import *

#Variaveis
DIRETORIA = "apps"
NOMES = os.listdir("apps")



#Busca das Aplicação dentro da diretoria
arquivos         = Buscar(NOMES)
class_Instalador = Instal_SHINC(DIRETORIA,NOMES,arquivos)

#Leitura do Arquivo de execução e separação de comandos
conteudo  = class_Instalador.LerArg()
posissao  = class_Instalador.SeparaComentario(conteudo)
comandos  = class_Instalador.LimpComentario(conteudo,posissao)

janela = Tk()
for c in range(0,len(NOMES)):
    a = class_Instalador.ExecutaComando(janela,comandos)
    a[NOMES[c]][0].pack()

janela.mainloop()































"""
janela = Tk()
btn = [Button(janela,text=NOMES[0],command=lambda: class_Instalador.ExecutaComando(comandos[NOMES[0]])),
       Button(janela,text=NOMES[1],command=lambda: class_Instalador.ExecutaComando(comandos[NOMES[1]]))]
btna = {}
for c in range(0,len(NOMES)):
    btna[NOMES[c]]= Button(janela,text=NOMES[c],command=lambda: os.startfile(f'apps\{NOMES[c]}\{NOMES[c]}.py'))
print(btn)
print(btna)

#for c in range(0,len(NOMES)):
btn[0].pack()
btn[1].pack()
btna['meuapp'].pack()
janela.mainloop()

"""



#Execução dos Arquivos
