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
                data = self.connection.recv(self.server.buffer_size)
                if not data: break;
                msg = str(self.address) + ":" + data.decode('utf-8')
                self.server.broadcast(msg)  # send to all clients connected
                print(msg)  # for server logging
            except ConnectionResetError:
                self.connection.close()
                self.server.broadcast(str(self.address) + " has disconnected.")
                print("Connection closed by client!")
                self.server.remove_client(self)
                return
        self.connection.close()
        self.server.broadcast(str(self.address) + " has disconnected.")
        print("Connection closed!")
        self.server.remove_client(self)
