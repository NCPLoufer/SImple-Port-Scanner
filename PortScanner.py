#!/usr/bin/python3

import socket
import sys
from datetime import datetime

ip = input('Enter the ip you want to scan: ')
RemoteIp = socket.gethostbyname(ip)

print('-' * 39)
print('Please wait, scanning IP on proccess...')
print('-' * 39)

t1 = datetime.now()

try:
    for port in range(1,1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        result = s.connect_ex((RemoteIp, port))
        if result == 0:
            print('Open Ports: ', port)
            s.close()

except KeyboardInterrupt:
    print('You pressed a wrong button')
    sys.exit()

except socket.gaierror:
    print('IP address could not be resolved. Quitting.')
    sys.exit()

except socket.error():
    print('Connection failed. Could not connect to the server.')
    sys.exit()

t2 = datetime.now()
Total_time = t2 - t1
print('Scanning for ip: ', ip + ' completed in: ', Total_time)
