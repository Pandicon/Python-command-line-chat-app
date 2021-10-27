import socket

from packet import Packet

class Client():
    def __init__(self, port, server_ip, disconnect_message, server_address, name) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.server_ip = server_ip
        self.disconnect_message = disconnect_message
        self.server_address = server_address
        self.client.connect(self.server_address)
        self.connected = True
        self.name = name

    def send(self, message: str, messageType: int = 1) -> None:
        packet = Packet(messageType, message, self.name)
        packed = packet.pack()
        self.client.send(packed)

    def receive(self, length: int = 1024) -> tuple:
        received_packet = self.client.recv(length)
        packet = Packet()
        return packet.unpack(received_packet)

    def disconnect(self):
        self.connected = False