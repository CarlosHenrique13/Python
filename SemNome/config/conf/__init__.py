from datetime import datetime
from config.user import *
import os


#Ler Arquivo de Configuração
def LerConf():
    arg = open("Proprietes\Configurete.conf")
    linhas = arg.readlines()
    linha = []
    for l in range(0,len(linhas)):
        linha.append(linhas[l][:len(linhas[l])-1].lower().split("="))
    return linha


#Analisar Se esta todu correto com a aplicação
def ConfigAnalise():
    #Pastas e pacote de Configuração
    if not os.path.exists("Proprietes"):
        os.makedirs("ProPrietes")
    #Informação da Instalação
    if not os.path.isfile("Proprietes/propriete.propri"):
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        arg = open("Proprietes/propriete.propri","wt+")
        arg.write(f"Data De Instalasao: {data}\n")
        arg.close()
    #Gera o Arq Configuração
    if not os.path.isfile("Proprietes/Configurete.conf"):
        arg = open("Proprietes/Configurete.conf","wt+")
        arg.write("loga=false\n")
        arg.close()
    #Gera o Arq Usuarios
    if not os.path.isfile("Proprietes/Usuario.user"):
        arg = open("Proprietes/Usuario.user","wt+")
        arg.write("------------- USUARIOS -------------\n")
        arg.write("Usuario=Root\n")
        arg.write("Passowrd=@Root0\n")
        arg.close()

   
    #ANALISAR OS COMANDOS DOS ARQUIVO CONF
    comando = LerConf()
    if comando[0][1] == "true":#Ser o login vor verdadeiro
       valor =  UesrConfirme()
    for c in range(0,len(comando)):
        for i in range(0,len(comando[c])):
            pass
            #print(comando[c][i])
            


    return False

 


