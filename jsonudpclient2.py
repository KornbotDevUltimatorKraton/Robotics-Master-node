import os
import json
import socket
import pickle
import subprocess
import multiprocessing

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Client side to receive the command to acticate restart loop
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
print("host ip: ", ip)  # Getting the host server ip
address = (ip, 5080)
sock.bind(address)

while True:
    data, addr = sock.recvfrom(4096)
    received = pickle.loads(data)
    message = json.loads(received)
    print(message, type(message), addr)
