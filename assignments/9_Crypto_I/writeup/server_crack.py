#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    with open('hashes.txt') as h:
        hashes = h.read().split("\n")[:-1]
    with open('passwords.txt') as p:
        passwords = p.read().split('\r\n')[:-1]
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    data = s.recv(1024)

    print(data[26:-5])

    for c in characters:
        for p in passwords:
            val = (c + p).strip()
            createdhash = hashlib.sha256(val.encode()).hexdigest()
            #print(repr(data[-69:-5]))
            if createdhash == data[-69:-5]:
                print(val + ": " + repr(createdhash))
                s.send(val + "\n")
                break
        
    #print(data)
    data = s.recv(1024)
    print(data[-69:-5])

    for c in characters:
        for p in passwords:
            val = (c + p).strip()
            createdhash = hashlib.sha256(val.encode()).hexdigest()
            if createdhash == data[-69:-5]:
                print(val + ": " + repr(createdhash))
                s.send(val + "\n")
                break

    data = s.recv(1024)
    print(data[-69:-5])

    for c in characters:
        for p in passwords:
            val = (c + p).strip()
            createdhash = hashlib.sha256(val.encode()).hexdigest()
            if createdhash == data[-69:-5]:
                print(val + ": " + repr(createdhash))
                s.send(val + "\n")
                break

    print(s.recv(1024))

if __name__ == "__main__":
    server_crack()
