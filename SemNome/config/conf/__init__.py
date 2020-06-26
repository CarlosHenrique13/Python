from datetime import datetime
import os


#Ler Arquivo de Configuração
def LerConf():
    arg= open("Proprietes\Configure.conf")
    linhas = arg.readlines()
    linha = []
    for l in range(0,len(linhas)):
        linha.append(linhas[l][:len(linhas[c]-1)])
    return linha

def Proprietes():
    arg = open("Proprietes\propriete.propri","wt+")
    arg.write(f"Data De Instalação={data}\n")
    arg.close()

#Analisar Se esta todu correto com a aplicação
def ConfigAnalise():
    #Pastas e pacote de Configuração
    if not os.path.exists("Proprietes"):
        os.makedirs("Proprietes")
    if not os.path.isfile("Proprietes\Configurete.conf"):
        arg = open("Proprietes\Configurete.conf","wt+")# EsCrever os Comandos
        data = datetime.date()
        
        arg.close()
    if not os.path.isfile("Proprietes\Usuario.user"):
        arg = open("Proprietes\Usuario.user")
        arg.write("======= USUARIOS =======\n")
        arg.write("Usuario=Root\n")
        arg.write("Passowrd=@Root0\n")
        arg.close()

    
    arg = open("Proprietes\Configurete.conf","wt+")
    arg.write()
    return False
    
    
    


