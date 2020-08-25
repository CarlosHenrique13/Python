from ftplib import FTP


class FTP():
    def Client(self, ip='', login='', password='', port=2121):
        """
        -> Cliente FTP
        :param login: Usuario do servido FTP
        :param password: Senha do Usuario
        :param ip: Host do servidor FTP
        :param port: Porta de comunicação con servidor.Padrão 2121
        :return: Conexão do FTP
        """
        try:
            handler = FTP(ip)
            handler.login(login, password)
            print('[+][FTP]Conectado')
            return handler
        except Exception:
            print('[-][FTP]Não foi possivel conectar ao servidor FTP Verefique se a internet')

    def Download(self, handler, dire, filename):
        """
        -> Downloads FTP
        :param handler: Servido FTP
        :param dire: Diretoria no servido para o download
        :param filename: Nome do arquivo que sera baixado com extensão
        :return: None
        """
        Dfile = open(f'{dire}/{filename}', 'wb')
        try:
            handler.retrbinary('RETR ' + filename, Dfile.write)
        except:
            print('[-][FTP]Erro ao abaixar o arquivo ')
        Dfile.close()
        print('[+][FTP]Download feito com sucesso!')

    def Upload(self, handler, name, path, local=dir):
        """
        -> Upload
        :param handler: Servidor FTP
        :param name: Nome do arquivo
        :param path: Nome do arquivo
        :param local: Local para armazenar o arquivo
        :return: None
        """
        try:
            handler.cwd(local)
            handler.storbinary('STOR ' + name, open(path, 'rb'), 1024)
            print(f'[+][FTP]Upload {name} feito com sucesso.')
        except:

            print('[-][FTP]Erro ao subir o arquivo ao servidor')
            return None
        print('[+][FTP]Operação efetuada com sucesso :)')

    def ListDirectories(self, ftp):
        """
        -> Listar Diretorias
        :param ftp: Servido Conectado
        :return: Pastas e Arquivos do Servido
        """
        log = []
        ftp.retrlines('LIST', callback=log.append)
        files = (line.rsplit(None, 1)[1] for line in log)
        arqs = []
        for f in list(files):
            arqs.append(f)
        return arqs

    def MoveToDir(self, handler, Dir):
        """
        -> Mover para Diretoria
        :param handler: Servido FTP
        :param Dir: Local para onde sera movido o arquivo no FTP
        :return: None
        """
        try:
            handler.cwd(Dir)
            print(f'[+][FTP]Movido arquivo: {Dir}')
        except Exception:
            print('[-][FTP]Não foi possivel acessar o diretorio!!')
    
    def MakeDir(self, handler, name):
        """
        -> Criar Diretorio
        :param handler: Servido FTP
        :param name: Nome do Diretorio
        :return: None
        """
        try:
            handler.mkd(name)
            print(f'[+][FTP]Diretorio {name} criado com sucessor.')
        except Exception:
            print('[-][FTP]Não foi possivel criar o diretorio ela ja existe!!')

    def DelFile(self, handler, name):
            """
            -> Deletar Arquivo
            :param handler: Servido FTP
            :param name: Nome do arquivo que deseja ser deletado
            :return: None
            """
            try:
                handler.delete(name)
                print('[+][FTP]O arquivo foi deletado')
            except Exception:
                print('[-][FTP]não foi possivel deletar o arquivo ou ele é inexistente')
