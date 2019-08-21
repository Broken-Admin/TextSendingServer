## TextSendingServer

+ Designed to send text information over a basic socket connection
+ Written in Python
+ Likely insecure

## Scripts

+ server.py - the main server python file
  + Hosted, by default, on the local machine
+ client.py - the client for connecting to the server, can be used from any device that can access the machine running the server script
  + LAN
  + WLAN
  + WAN

## Known bugs
+ Does not work over LAN
  + Possibly over WLAN and WAN, similarly
  + Only works locally?

## To-Do
+ Monitor Packets with Wireshark and verify or debunk possible insecurity 
