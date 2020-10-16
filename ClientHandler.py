import threading
import Server


class ClientHandler(threading.Thread):
    def __init__(self, connection, address, server):
        self.server = server
        self.connection = connection
        self.address = address

    def run(self):

