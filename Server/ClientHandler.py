import threading


class ClientHandler(threading.Thread):
    def __init__(self, connection, address, server):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address
        self.server = server
        print("Starting new Client Handler")
        self.start()

    def send_msg(self, msg: str):
        self.connection.send(msg.encode('utf-8'))

    def run(self):
        while 1:
            try:
                data = self.connection.recv(BUFFER_SIZE)
                if not data: break;
                print(str(address) + data.decode("utf-8"))
                self.connection.send(b'Server: ' + data)
            except ConnectionResetError:
                self.connection.close()
                print("Connection closed by client!")
                self.server.remove_client(self)
                return
        self.connection.close()
        print("Connection closed!")
        self.server.remove_client(self)
