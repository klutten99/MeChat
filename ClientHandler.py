import _thread
import Server


class ClientHandler:
    def run(self):
        while 1:
            try:
                data = self.connection.recv(self.server.buffer_size)
                if not data: break;
                print(data.decode("utf-8"))
                self.connection.send(b'Server: ' + data)
            except ConnectionResetError:
                self.connection.close()
                print(str(address) + " has lost connection.")
                return
        self.connection.close()
        print(str(address) + " has disconnected.")

    def __init__(self, connection, address):
        self.server = server
        self.connection = connection
        self.address = address
        _thread.start_new_thread(run, ())

