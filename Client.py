import socket
import threading

from Account import Account


class Client:
    def __init__(self, port=1337, host="127.0.0.1", buffer_size=1024):
        self.port = port
        self.host = host
        self.buffer_size = buffer_size
        self.account = Account(input("Name: "), input("Username: "), input("Password: "))

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Connecting to host...")
        self.sock.connect((self.host, self.port))
        print("Connected to host! (" + self.host + ":" + str(self.port) + ")")

        self.setup_account()

        self.input_handler = InputHandler(self)
        self.message_handler = MessageHandler(self)
        print("Client initiated!")

    def setup_account(self):
        self.send_msg(Account.magic + str(self.account))

    def send_msg(self, msg: str):
        self.sock.send(msg.encode('utf-8'))


class InputHandler(threading.Thread):
    def __init__(self, client: Client):
        threading.Thread.__init__(self)
        self.client = client
        self.start()
        print("Started input handler!")

    def run(self):
        while 1:
            message = input()
            if len(message.encode('utf-8')) > self.client.buffer_size:
                print("ERROR: Message too big!")
            else:
                self.client.send_msg(message)


class MessageHandler(threading.Thread):
    def __init__(self, client: Client):
        threading.Thread.__init__(self)
        self.client = client
        self.start()
        print("Started message handler!")

    def run(self):
        while 1:
            message = self.client.sock.recv(self.client.buffer_size)
            print(message.decode('utf-8'))

Client()