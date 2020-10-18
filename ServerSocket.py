import _thread
import socket

PORT = 1337
HOST = '127.0.0.1'
MAX_CONNECTIONS = 3
BUFFER_SIZE = 1024

connections = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(MAX_CONNECTIONS)


def log_conn(conn):
    while 1:
        try:
            data = conn.recv(BUFFER_SIZE)
            if not data: break;
            print(data.decode("utf-8"))
            conn.send(b'Server: ' + data)
        except ConnectionResetError:
            conn.close()
            print("Connection closed by client!")
            return
    conn.close()
    print("Connection closed!")


def accept_connections():
    print("Waiting for connections...")
    while 1:
        conn, addr = s.accept()
        connections.append((conn, addr))
        print("Connection found! Address: " + str(addr))
        _thread.start_new_thread(log_conn, (conn,))
        print("Started new thread for connection")
        # conn.send(b'You have been connected!\n')

accept_connections()
