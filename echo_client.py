# -*- coding: utf-8 -*-
from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from base64decoder import myBase64

class EchoClient():
    def __init__(self, host,
                 port=80):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect((host, port))
        
    def send_message(self, message):
        err = self.socket.sendall(message)
        
        if err:
            return False
        
        return True
    
    def receive_message(self, expected_msg_len):
        received_data = ''
        while len(received_data) < expected_msg_len:
            received_data += self.socket.recv(4096)
            print 'Klient odebrał:', received_data
        
        self.socket.close()    
        return received_data
    
if __name__ == '__main__':
    host = raw_input('Podaj IP hosta: ')
    mybase64 = myBase64()

    while True:
        operation = int(raw_input('\
                                    1 - Przeslij tekst\n\
                                    2 - Przeslij plik\n\
                                    0 - Zakoncz\n\
                                    Podaj numer operacji: '))
        if operation == 1:
            to_encode = raw_input('Wpisz tekst: ')
            encoded_data = mybase64.my_base64encode(to_encode)
            echoClient = EchoClient(host)
            res = echoClient.send_message(encoded_data)
            
            if res:
                received_data = echoClient.receive_message(len(encoded_data))
                decoded_data = mybase64.my_base64decode(received_data)
                print 'odebrany i odkodowany tekst:', decoded_data
                
        elif operation == 2:
            file_path = raw_input('Podaj sciezke do pliku: ')
            
            f = open(file_path, 'rb')
            to_encode = f.read()
            f.close()
            
            encoded_data = mybase64.my_base64encode(to_encode)
            
            echoClient = EchoClient(host)
            res = echoClient.send_message(encoded_data)
            
            if res:
                received_data = echoClient.receive_message(len(encoded_data))
                decoded_data = mybase64.my_base64decode(received_data)
                ext = file_path[file_path.index('.'):]
                
                f = open('decoded_data'+ext, 'wb')
                f.writelines(decoded_data)
                f.close()

        else:
            break
            