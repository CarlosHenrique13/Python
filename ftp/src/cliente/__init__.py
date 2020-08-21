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
