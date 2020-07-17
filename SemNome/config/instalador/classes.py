

#Classe para leitura dos aruivos
class Instal_SHINC():
    import os.path
    #Main
    def __init__(self,diretoria,nomes,arquivos):
        #Variaveis Globais
        self.diret = diretoria
        self.names = nomes
        self.arq = arquivos
        print("=============================================== Instal_SHINC ===============================================")

    #Ler os Arquivos
    def LerArg(self):
        arquivos = {}
        for c in range(0,len(self.names)):
            arquivo = open(f"{self.diret}/{self.names[c]}/{self.arq[self.names[c]]}",'rt')
            linhas = arquivo.readlines()
            temp = []
            for l in range(0,len(linhas)):
                temp.append(linhas[l][:len(linhas[l])-1])
            arquivos[self.names[c]] = temp
        print(f"[LerArg] Dicionario: {arquivos}")
        return arquivos

    #Separa os Comentario
    def SeparaComentario(self,ler_arg):
        posisao = {}
        for c in range(0,len(ler_arg.keys())):
            pos = []
            temp = []
            #Ler as linhas e colocar a posição do simbolo <// //> de comentario
            for l in range(0,len(ler_arg[self.names[c]])):
                #print(f'[ValidaArg] Linhas: {ler_arg[self.names[c]][l]}')
                if ler_arg[self.names[c]][l][0:3] in '<//':
                   pos.append(l)
                elif ler_arg[self.names[c]][l][len(ler_arg[self.names[c]][l])-3:] == '<//':
                    pos.append(l)
                elif ler_arg[self.names[c]][l] in '//>':
                    pos.append(l)
                elif ler_arg[self.names[c]][l][len(ler_arg[self.names[c]][l])-3:] == '//>':
                    pos.append(l)
                else:
                    temp.append(ler_arg[self.names[c]][l])
            posisao[self.names[c]] = [pos,temp]
        print(f'[SeparaComentario] Dicionario: {posisao}')
        return posisao

    # Limpar Comentario
    def LimpComentario(self,ler_arg,posisao):
        comandos = {}
        #Monatar as cordenadas dos comentarios
        for c in range(0,len(ler_arg.keys())):
            for l in range(0,len(posisao[self.names[c]])):
                try:
                    valor = abs(int(posisao[self.names[c]][l][0]) - int(posisao[self.names[c]][l][1]))
                    posisao[self.names[c]][1].pop(posisao[self.names[c]][l][0])
                    #Remover texto do comentario
                    for r in range(len(posisao[self.names[c]][l]),valor):
                        posisao[self.names[c]][1].pop(posisao[self.names[c]][l][0])
                    #Escrever os comandos no dicionario
                    time = []
                    for esc in range(0,len(posisao[self.names[c]][1])):
                        time.append(posisao[self.names[c]][1][esc])
                    print(f'[LimpComentario] Arquivo: {self.names[c]} Comandos: {time}')
                    comandos[self.names[c]] = time
                except(ValueError):
                   pass
                except(IndexError):
                    comandos[self.names[c]] = None
                    print(f'[LimpComentario] Erro Arquivos Vazio {self.names[c]}.inst')
        print(f'[LimpComentario] Dicionario: {comandos}')
        return comandos

    # Valida os Comandos do Arquivo
    def ExecutaComando(self,janela,comand):
        #Programa sendo separado para cada comando
        comandos = Comandos(self.names,self.diret,janela,comand)
        butaos = comandos.Validar()
        comando = {}
        #Descompact os botaos
        for c in range(0,len(self.names)):
            temp0 = []
            for l in range(0,len(butaos[self.names[c]])):
                for i in range(0, len(butaos[self.names[c]][l])):
                    for f in range(0,len(butaos[self.names[c]][l][i])):
                        temp0.append(butaos[self.names[c]][l][i][f])

            comando[self.names[c]] = temp0
        return  comando


    #Listar os arquivo que estão istalados
    def ArgApps(self):
        pass

    print("-------------------------------------------------------------------------------------------------------")


#Executador de comandos da Classe Instal_SHINC
class Comandos():
    # Importação de pacotes
    import os
    from tkinter import Button

    #Main
    def __init__(self,nomes,diretoria,janela,comandos):
        self.name = nomes
        self.comand = comandos
        self.direct = diretoria
        self.tela = janela
        print("==================================== Comandos ====================================")

    #Valida os Comandos
    def Validar(self):
        apps = {}
        comando = {}
        #Descompactar para saber quandos itens estão no comando
        for c in range(0,len(self.comand)):
            temp = []
            for l in range(0,len(self.comand[self.name[c]])):
                temp.append(self.comand[self.name[c]][l].split(" "))
                #print(self.comand[self.name[c]][l].split(" "),self.name[c])
            apps[self.name[c]] = temp

        #print(apps)
        for c in range(0,len(apps)):
            temp = []
            for l in range(0,len(apps[self.name[c]])):
                #print(self.name[c],len(apps[self.name[c]][l]),apps[self.name[c]][l])
                if len(apps[self.name[c]][l]) == 1:
                    print(self.name[c],self.ComandSimple(apps[self.name[c]][l]))
                else:
                     #print(self.name[c],self.ComandCaretes(apps[self.name[c]][l],self.name[c]))
                     temp.append(self.ComandCaretes(apps[self.name[c]][l], self.name[c]))
            comando[self.name[c]] = temp
        return comando

    # Comandos Simples
    def ComandSimple(self,comando):
        return "Vazio"

    # Comandos com mais de um carater
    def ComandCaretes(self,comando,name):
        #print(len(comando),comando,name)
        comandos = []
        #Comandos
        if comando[0] == "@Start":
            if f'{name}.exe' in  self.os.listdir(f'{self.direct}\{name}'):
                comandos.append(self.Start(name, comando[1], fr"{name}\{name}.exe"))
            else:
                comandos.append(self.Start(name,comando[1],fr"{name}\{name}.py"))
        elif comando[0] == "@Name":
            comandos.append(self.Name(comando[1]))
        return comandos

    #Comando Start
    def Start(self,name,valida,diretoria):
        comando = []
        if valida.lower() == "on":
            comando.append(self.Button(self.tela,text=name,command=lambda: self.os.startfile(fr'{self.direct}\{diretoria}')))
        elif valida.islower() == "of":
            print("[Start]Não foi executado o comando @Start")
        else:
            print("[Start] Comando prenxido incorretamente")
        return comando
    #Comando Name
    def Name(self,comand):
        comando = []
        comando.append(comand)
        return comando
