import threading


class ClientHandler(threading.Thread):
    def __init__(self, connection, address, server, account):
        threading.Thread.__init__(self)
        self.account = account
        self.connection = connection
        self.address = address
        self.server = server
        print("Starting new Client Handler")
        server.broadcast(account.username + " connected to the room.")
        self.start()

    def send_msg(self, msg: str):
        self.connection.send(msg.encode('utf-8'))

    def run(self):
        while 1:
            try:
                data = self.connection.recv(self.server.buffer_size)
                if not data: break;
                msg = str(self.account.username) + ": " + data.decode('utf-8')
                self.server.broadcast(msg, self)  # send to all clients connected
                print(msg)  # for server logging
            except ConnectionResetError:
                self.connection.close()
                self.server.remove_client(self)
                self.server.broadcast(str(self.account.username) + " has disconnected.")
                print("Connection closed by client!")
                return
        self.connection.close()
        self.server.remove_client(self)
        self.server.broadcast(str(self.account.username) + " has disconnected.")
        print("Connection closed!")
