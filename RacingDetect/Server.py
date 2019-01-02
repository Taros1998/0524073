import socket
import numpy as np
from flask import Flask
import json

UDP_IP = "0.0.0.0"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
count = 0
while True:
    count += 1
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print(data)
    if count == 10:
        break

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def Map():
    return data

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
