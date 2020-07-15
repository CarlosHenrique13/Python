# Pacotes Usados
from config.instalador.classes import *
import os


def Buscar(pasta, raiz_apps):
    def AppsConteudo(pasta_raiz, pasta):
        """
        -> Conteudo das pastas de Aplicativos
        :param pasta: Local da pasta raiz onde estar os aplicativos
        :return: O conteudo da pasta que foi digitado em <apps>
        """
        try:
            aplicativos_diretoria = {}
            # Ler arquivos dentro da pasta do app
            for c in range(0, len(pasta_raiz)):
                # print(f'Valores: {apps[c]} Dentro: {os.listdir(f"apps/{apps[c]}")} ... AppsConteudo')
                aplicativos_diretoria[pasta_raiz[c]] = os.listdir(f"{pasta}/{pasta_raiz[c]}")
            print(f"[AppsConteudo] Pastas: {pasta_raiz}")
            return aplicativos_diretoria
        except:
            print("[AppsConteudo] Erro Inesperado")

    def Busca_shinc(pasta_raiz, nome):
        """
        -> Separador de Extensão
        :param nome: Conteudo que foi retornado de  AppsConteudo
        :param pasta_raiz: Local da pasta raiz onde estar os aplicativos
        :return: um dicionario com listas de arquivos da pasta
        """
        aplicativo_aruivos = {}
        try:
            # Procura o arquivo .shinc
            for c in range(0, len(pasta_raiz.keys())):
                temp = []
                # separa as extensão dos arquivos
                for itens in range(0, len(pasta_raiz[nome[c]])):
                    if 2 == len(pasta_raiz[nome[c]][itens].split(".")):
                        # print(f'[Busca_shinc] Pasta: {apps[c]} Arquivo: {pasta_raiz[apps[c]][itens]}')
                        temp.append(pasta_raiz[nome[c]][itens].split("."))
                    else:
                        print(f'[Busca_shinc] Pasta: {nome[c]} Sub Pasta: {pasta_raiz[nome[c]][itens]}')
                aplicativo_aruivos[nome[c]] = temp
            return aplicativo_aruivos
        except:
            print("[Busca_shinc] Erro Inesperado")

    def Mont_shinc(arq_extensao, nomes):
        """
        -> Montador de Extensão
        :param arq_extensao: onteudo que foi retornado de  Busca_shinc
        :param nomes: nomes dos aplicativos
        :return: Dicionario com o nome dos aplicativo contendo o nome do arquivo de Inicialização
        """
        args = {}
        try:
            # Juntar a extensão com o nome do arquivo para compara se a o arquivo de Inicialização
            for c in range(0, len(arq_extensao)):
                for intes in range(0, len(arq_extensao[nomes[c]])):
                    try:
                        for extensao in range(0, int(len(arq_extensao[nomes[c]][intes]) / 2)):
                            # print(f"[Mont_shinc] Pasta: {nomes[c]} Arquivo: {arq_extensao[nomes[c]][intes][extensao]}."
                            #     f"{arq_extensao[nomes[c]][intes][extensao+1]}")
                            if arq_extensao[nomes[c]][intes][extensao + 1] == "shinc":
                                args[nomes[
                                    c]] = f'{arq_extensao[nomes[c]][intes][extensao]}.{arq_extensao[nomes[c]][intes][extensao + 1]}'
                    except:
                        print("[Mont_shinc] Erro algum arquivo ou pasta foi executado nesta area sem ter extensão")
            if args != len(nomes):
                # Se não ouver o arquivo de Inicialização prencher com none o valor do aplicativo
                for names in range(0, len(nomes)):
                    if not nomes[names] in args.keys():
                        args[nomes[names]] = None
            print(f'[Mont_shinc] Dicionario: {args}')
            return args
        except:
            print("[Mont_shinc] Erro Inesperado")

    print("================================================= Funções =================================================")
    # Controle
    fun1 = AppsConteudo(raiz_apps, pasta)
    fun2 = Busca_shinc(fun1, raiz_apps)
    fun3 = Mont_shinc(fun2, raiz_apps)
    # Limpeza dos dicionarios
    fun1.clear()
    fun2.clear()
    print("===========================================================================================================")
    return fun3


def Instlador(janela, DIRETORIA):
    # Variaveis
    NOMES = os.listdir(DIRETORIA)

    # Busca das Aplicação dentro da diretoria
    arquivos = Buscar(DIRETORIA, NOMES)
    class_Instalador = Instal_SHINC(DIRETORIA, NOMES, arquivos)

    # Leitura do Arquivo de execução e separação de comandos
    conteudo = class_Instalador.LerArg()
    posissao = class_Instalador.SeparaComentario(conteudo)
    comandos = class_Instalador.LimpComentario(conteudo, posissao)

    for c in range(0, len(NOMES)):
        button = class_Instalador.ExecutaComando(janela, comandos)
        button[NOMES[c]][0].grid(row=1,column=c)

