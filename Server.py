import socket
import threading
from ClientHandler import ClientHandler


class Server(threading.Thread):
    clients = []

    def __init__(self, port=1337, host="127.0.0.1", buffer_size=1024, max_connections=3):
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.buffer_size = buffer_size
        self.max_connections = max_connections

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(5)
        print("Server initiated!")
        print("Starting server thread..")
        self.start()

    def run(self):
        print("Started server thread!")
        print("Accepting incoming connections...")
        while 1:
            connection, address = self.sock.accept()
            if len(self.clients) < self.max_connections:
                client = ClientHandler(connection, address, self)
                self.clients.append(client)
                print(str(address) + " connected to the server.")
            else:
                connection.send(b'Too many are connected to this server already! ('
                                + str(len(self.clients)).encode('utf-8')
                                + b'/'
                                + str(self.max_connections).encode('utf-8') + b')')
                connection.close()
                print("Rejected client trying to connect. Max connections reached!")
