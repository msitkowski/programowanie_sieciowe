# -*- coding: utf-8 -*-
from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from socket import gethostname
from thread import start_new_thread

class EchoServer():
    def __init__(self, port=80):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind((gethostname(), port))
        self.server_socket.listen(5)
        print 'Serwer:', gethostname(), 'nasluchuje na porcie:', port
    
    def echo(self, client_socket):
        while True:
            received_data = client_socket.recv(4096)
            print 'Serwer odebral:', received_data
            client_socket.sendall(received_data)
            
            if not received_data:
                break
            
        client_socket.close()
        
if __name__ == '__main__':
    echoServer = EchoServer()
    
    while True:
        client_socket, host = echoServer.server_socket.accept()
        start_new_thread(echoServer.echo, (client_socket,))
        
    echoServer.server_socket.close()
    