#Locais
from func import *
from classes import *

#Externas
import os


#Variaveis
DIRETORIA = "apps"
NOMES = os.listdir("apps")


#Busca das Aplicação dentro da diretoria
arquivos         = Buscar(NOMES)
class_Instalador = Instal_SHINC(DIRETORIA,NOMES,arquivos)

#Leitura do Arquivo de execução e separação de comandos
conteudo = class_Instalador.LerArg()
posisao  = class_Instalador.SeparaComentario(conteudo)
comando  = class_Instalador.LimpComentario(conteudo,posisao)

#Execução dos Arquivos
