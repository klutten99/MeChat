import _thread
import socket
import time

PORT = 1337
HOST = '127.0.0.1'
MAX_RETRIES = 3
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connecting to host...")
s.connect((HOST, PORT))
print("Connected to host!" + HOST + ":" + str(PORT))
"""
retry = 1
while 1:
    try:
        s.connect((HOST, PORT))
    except ConnectionRefusedError:
        if retry > 3:
            print("Can't connect to server! Check your ip and port.")
            exit()
        print("Couldn't connect to server retrying in 5 seconds. (" + str(retry) + "/" + str(MAX_RETRIES) + ")")
        retry += 1
        time.sleep(5)
"""


def msgLoop():
    while 1:
        m = input()
        s.send(bytes(m, 'utf-8'))


_thread.start_new_thread(msgLoop, ())
while 1:
    r = s.recv(BUFFER_SIZE)
    print(r.decode('utf-8'))
