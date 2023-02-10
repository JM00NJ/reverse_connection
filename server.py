import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.1"  # Change this
port = 3334  # Change this

try:
    s.bind((host, port))
    try:
        s.listen(1)
        print("Started for listening...")
        conn, address = s.accept()
    except socket.error as error:
        s.close()
    print("Listening...")
except socket.gaierror as error:
    print("Got error while connecting server:: " + error)
    s.close()


def recv_msg():
    raw_data = conn.recv(8192)
    packet = raw_data.decode("utf-8")
    print("Output: " + packet)


def send_msg():
    try:
        cmd = str(input(":>"))
        conn.send(cmd.encode("ascii"))
    except KeyboardInterrupt:
        s.close()
        print("Connection Closed!")
        time.sleep(2)
        exit()


while True:
    thread_1 = threading.Thread(target=send_msg())
    thread_2 = threading.Thread(target=recv_msg())
    thread_1.start()
    thread_2.start()
