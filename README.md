# Python command line chat app
 
This project is a sub-project to a [multiplayer game](https://github.com/Pandicon/Multiplayer-Game) I'm creating with my friend. It basically allows you to chat with other people **that are on the same LAN**.

## Setup
### Server
If you are a little lucky, you won't need any setup for the server. Just go to the server folder and run the `main.py` file. You might have to disable firewall for it to work correctly, but if that is the case, Windows will most likely tell you to do so.<br>
If the console says `Server is listening on IP xyz and port xyz`, you are good to go, just give the IP and port to all people that would like to join the chat. The IP is your local IP, that's why it only works on your LAN.<br>
The server might also crash when you try to start it up. If it says that there is usually only one connection allowed on one port or something like that, go to the root folder and change the `PORT` property in the `config.json` file and try again (disclaimer: ports like 0001, 9999 etc. will most likely be taken by a different process, I recommend you try some random looking ports like 4876 etc.). Change the ports until it works and then give the IP and port to all people you want to join. If there is a different error than the port one, then you are on your own. :D

### Client
If you know that a server is running on your LAN, ask for the IP and port of the server. Then go to the root folder of this app and fill in the `SERVER_IP` and `PORT` properties in the `config.json` file with the IP and port of the server. After you do that, go to the client folder, run the main.py file, and enjoy your chat with others. :D
