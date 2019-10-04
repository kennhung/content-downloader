# -*- coding: utf-8 -*-

import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080)) # here you must past the public external ipaddress of the server machine, not that local address

s.send(pickle.dumps({"url":"https://http.cat/400"}))

f = open("icon_2.jpg", "wb")
data = None
while True:
    m = s.recv(1024)
    data = m
    if m:
        f.write(data)
    else:
        break
f.write(data)
f.close()
print("Done receiving")