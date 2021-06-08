#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input('Enter the ip address you want to scan: ')
print('The ip address you want to scan is: ', host)

port = int(input('Enter the port you want to scan: '))
print('The port you want to scan is: ', port)

def portScanner(port):
    if s.connect_ex((host, port)):
        print('The port is closed')
    else:
        print('The port is open')

portScanner(port)


#ready--> Simple port scanner

