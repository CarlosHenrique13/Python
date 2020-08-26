import socket

def Server(self,host="127.0.0.1",porta=8585):
        """
        -> Servido TCP
        :param host: Ip para o Servido
        :param porta: Porta de Comunicação
        :return: None
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        msg = f"[+]Você se conector ao {host}."
        s.bind((host, porta))
        s.listen(1)
        while True:
            c, e = s.accept()
            print("Conectado com ", e)
            c.send(msg.encode('ascii'))
            c.close()