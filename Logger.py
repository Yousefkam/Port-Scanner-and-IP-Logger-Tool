import socket
import os
import requests
import sys
import urllib 
import time
from datetime import datetime as dt
from urllib import request as urlrequests

def logger():
    s = socket.socket()
    personal_ip = input("Enter your IP address: ")
    attack_port = input("Enter desired port (Standard is 80): ")

    try:
        host = personal_ip
        port = attack_port
        
        s.bind((host, int(port)))

    except:
        print("Error has occured, try another address.")

    while True:
        try: 
            s.listen(5)
            conn, address = s.accept()

            print(f"[+] IP Logged {str(address[0])} at {str(dt.now)}")

        except KeyboardInterrupt:
            print("^C detected, shutting down.")
            sys.exit()
        except:
            pass
            print("Error detected, shutting down.")
            sys.exit(0)

logger()