'''
Program Name: Program12_5.py
Prgram Description: This program reads lines from the mbox-short.txt file and displays how many messages were sent on a specific date.
Programmer: Ray, Stephen
Date: 03/28/2022
Course: CSC233-1L1
'''

import socket

def main():    

    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    my_sock.send(cmd)

    #Find the header of the url to exclude it
    data = my_sock.recv(512)
    headerData = data.decode()
    headerEnding = headerData.find('\r\n\r\n') + 4
    
    print(headerData[headerEnding:], end='')

    while True:                                 
        data = my_sock.recv(512)
        if not data:
            break
        print(data.decode())
    my_sock.close()
    
#Call the main() function
main()