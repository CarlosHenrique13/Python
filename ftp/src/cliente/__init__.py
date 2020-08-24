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