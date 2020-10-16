import socket


class Server:
    connections = []
    def __init__(self, port=1337, host="127.0.0.1", buffer_size=1024, max_connections=3):
        self.port = port
        self.host = host
        self.buffer_size = buffer_size
        self.max_connections = max_connections

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen()

    def