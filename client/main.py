import threading

from configHandler import loadConfigData
from clientClass import Client

def main():
    mainConfig = loadConfigData("../config.json")
    PORT = mainConfig["PORT"]
    SERVER_IP = mainConfig["SERVER_IP"]
    DISCONNECT_MESSAGE = mainConfig["DISCONNECT_MESSAGE"]
    SERVER_ADDRESS = (SERVER_IP, PORT)

    NAME = input("What is your nickname?\n")
    
    client = Client(PORT, SERVER_IP, DISCONNECT_MESSAGE, SERVER_ADDRESS, NAME)
    sending_messages_thread = threading.Thread(target=send_messages, args=(client,))
    sending_messages_thread.start()
    receiving_messages_thread = threading.Thread(target=receive_messages, args=(client,))
    receiving_messages_thread.start()
    client.send(NAME, 2)

def send_messages(client):
    while client.connected:
        client.send(input())

def receive_messages(client):
    while client.connected:
        author, responseType, response = client.receive(1024)
        print(f"[{author}] {response}")
        if not responseType:
            client.disconnect()

if __name__ == "__main__":
    main()