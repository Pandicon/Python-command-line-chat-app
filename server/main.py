import socket
import threading

from packet import Packet
from configHandler import loadConfigData

allConnections = []
nicks = {}

def main():
    mainConfig = loadConfigData("../config.json")
    PORT = mainConfig["PORT"]
    SERVER_IP = socket.gethostbyname(socket.gethostname())
    DISCONNECT_MESSAGE = mainConfig["DISCONNECT_MESSAGE"]
    SERVER_ADDRESS = (SERVER_IP, PORT)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(SERVER_ADDRESS)

    print("[STARTING] Server is starting...")

    server.listen()
    print(f"[LISTENING] Server is listening on IP {SERVER_IP} and port {PORT}")

    while True:
        connection, address = server.accept()
        allConnections.append([connection, address])
        thread = threading.Thread(target=handleClient, args=(connection, address, DISCONNECT_MESSAGE))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

def handleClient(connection: socket.socket, address, disconnect_message):
    print(f"[NEW CONNECTION] {address} connected.")
    nick = ""
    firstNick = True

    connected = True
    while connected:
        author, messageType, message = receive(connection, 1024)
        if not messageType:
            print(f"[DISCONNECT] Disconnecting {address} due to invalid message")
            connected = False
            send(connection, "Disconnecting due to receiving invalid message", 0)
            break
        if message == disconnect_message:
            print(f"[DISCONNECT] Message to disconnect received, disconnecting {address}")
            connected = False
            send(connection, "Disconnecting due to your request", 0)
            sendAll("SERVER", f"{nicks[(connection, address)]} left", 1, [[connection, address]])
            break
        if messageType == 2:
            nick = message
            nicks[(connection, address)] = nick
            send(connection, "Nickname received", 255)
            print(f"[NICKNAME] {message}")
            if firstNick:
                send(connection, f"You joined", 1)
                sendAll("SERVER", f"{nick} joined", 1, [[connection, address]])
                firstNick = False
            continue

        print(f"[{author}] {message}")
        send(connection, "Message received", 255)
        if messageType == 1:
            sendAll(nicks[(connection, address)], message, 1, [[connection, address]])

    allConnections.remove([connection, address])
    connection.close()

def send(connection: socket.socket, message: str, messageType: int, author = "SERVER"):
    packet = Packet(messageType, message, author)
    packed = packet.pack()
    connection.send(packed)

def sendAll(author, message: str, messageType: int = 1, exclude: list = []):
    for connection in allConnections:
        if connection in exclude:
            continue
        send(connection[0], message, messageType, author)

def receive(connection: socket.socket, length: int):
    received_packet = connection.recv(length)
    packet = Packet()
    return packet.unpack(received_packet)

if __name__ == "__main__":
    main()