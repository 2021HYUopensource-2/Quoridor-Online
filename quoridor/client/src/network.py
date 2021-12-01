"""
Quoridor Online
Quentin Deschamps, 2020
"""
import socket
import pickle


class Network:
    """Manage communication between client and server"""
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)

    def connect(self):
        """adress에 맞추어 서버에 연결시킨다"""
        try:
            self.client.connect(self.addr)
        except socket.error as e:
            print(e)

    def recv(self):
        """recv해서 데이터를 받은 뒤 decode로 해석하고 ;에 맞추어 나누어서 return"""
        try:
            return self.client.recv(2048).decode().split(';')
        except socket.error as e:
            print(e)

    def send(self, data):
        """encode로 데이터를 변환한 뒤 보낸다"""
        try:
            self.client.send(str.encode(data))
        except socket.error as e:
            print(e)

    def get_game(self):
        """recv해서 받은 데이터를 pickle로 로드해서 return"""
        return pickle.loads(self.client.recv(2048))
