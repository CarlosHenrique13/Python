from datetime import datetime
import os


#Ler Arquivo de Configuração
def LerConf():
    arg = open("Proprietes\Configurete.conf")
    linhas = arg.readlines()
    linha = []
    for l in range(0,len(linhas)):
        linha.append(linhas[l][:len(linhas[l])-1].split("="))
    return linha

#Propriedades de Quado Foi Instalado são Informação
def Proprietes(data):
    arg = open("Proprietes\propriete.propri","wt+")
    arg.write(f"Data De Instalação={data}\n")
    arg.close()

#Analisar Se esta todu correto com a aplicação
def ConfigAnalise(raiz):
    #Pastas e pacote de Configuração
    if not os.path.exists("Proprietes"):
        os.makedirs("ProPrietes")

    if not os.path.isfile("Proprietes\Configurete.conf"):
        arg = open("Proprietes\Configurete.conf","wt+")
        arg.write("loga=false\n")
        arg.close()

   

   
    print(LerConf())
    return False

 
#def Or(): 
#    if not os.path.isfile("os\Proprietes\Usuario.user"):
#        arg = open("Proprietes\Usuario.user")
#        arg.write("======= USUARIOS =======\n")
#        arg.write("Usuario=Root\n")
#        arg.write("Passowrd=@Root0\n")
#        arg.close()

