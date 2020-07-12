

#Classe para leitura dos aruivos
class Instal_SHINC():
    #Main
    def __init__(self,diretoria,nomes,arquivos):
        #Variaveis Globais
        self.diret = diretoria
        self.names = nomes
        self.arq = arquivos

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
        print("-------------------------------------------------------------------------------------------------------")
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
                    print(f'[LimpComentario] Erro Arquivos Vazio {self.names[c]}.shinc')
        print(f'[LimpComentario] Dicionario: {comandos}')
        return comandos

    # Valida os Comandos do Arquivo
    def ValidaArg(self, ler_arg):
        pass

    #Listar os arquivo que estão istalados
    def ArgApps(self):
        pass


