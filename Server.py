import socket
import threading

from Account import Account
from ClientHandler import ClientHandler

DEBUG = True


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
                account = self.login_client(connection)
                if account is not None:
                    client = ClientHandler(connection, address, self, account)
                    self.clients.append(client)
                    print(str(address) + " connected to the server.")
                    print("Room is " + str(len(self.clients)) + "/" + str(self.max_connections))
                else:
                    print(str(address) + " tried to login")
            else:
                connection.send(b'Too many are connected to this server already! ('
                                + str(len(self.clients)).encode('utf-8')
                                + b'/'
                                + str(self.max_connections).encode('utf-8') + b')')
                connection.close()
                print("Rejected client trying to connect. Max connections reached!")

    # Sends a message to all clients connected to the server
    def broadcast(self, msg: str, *exclude: ClientHandler):
        clients = self.clients.copy()
        for client in exclude:
            clients.remove(client)

        for client in clients:
            client.send_msg(msg)

    def remove_client(self, client: ClientHandler):
        self.clients.remove(client)
        if DEBUG:
            print("Removed a client from the servers clients.")

    def login_client(self, connection):
        try:
            data = connection.recv(self.buffer_size)
            if not data:
                return None
            username, password = data.decode('utf-8').split(':')
            return Account(username, password)
        except ConnectionResetError:
            connection.close()
            print("Connection closed by client when trying to login!")
            return None


Server()
