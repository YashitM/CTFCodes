from random import randint
from time import sleep, time 
import sys
import signal
import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.126.135",8081))
s.listen(1) #listening for only one client
conn,addr=s.accept() 

flag = False

conn.send("\nSo here's a task for you:\n")
conn.send
conn.send("\nI will give you a set of numbers, you've got to tell me the smallest number among all of them!\n")
conn.send
conn.send("\nHere's an example: \n")
conn.send
conn.send("\n[222, 13, 12, 23, 14]\n")
conn.send
conn.send("\nThe expected input must be: 12\n")
conn.send
conn.send("\nYou have 10 seconds to answer each question\n")
conn.send
sleep(10)
x=randint(1,99)
conn.send ("Enter the number " + str(x) + " to start: "),

TIMEOUT1 = 15
TIMEOUT2 = 10

def interrupted(signum, frame):
	conn.send('\nSorry. Times up.\n')
	os._exit(0)

signal.signal(signal.SIGALRM, interrupted)

def input():
	try:
		foo = conn.recv(10)
		#foo = raw_input()
		return foo
	except:
		return

def factors(a):
	
	

signal.alarm(0)
ans1 = ""
signal.alarm(TIMEOUT1)
ans1 = input()
if(ans1!=None):
	if(int(ans1) == x):
		signal.alarm(0)
		for i in range (150):
			l = list()
			if(i<20):
				for j in range (5):
					l.append(randint(1,100))
			elif(i<30):
				for j in range (25):
					l.append(randint(1,1000))
			elif(i<50):
				for j in range (60):
					l.append(randint(1,10000))
			elif(i<70):
				for j in range (100):
					l.append(randint(1,100000))
			else:
				for j in range(200):
					l.append(randint(1,1000000))
			minimum = min(l)
			conn.send(str(l) + "\n")
			ans = ''
			signal.alarm(TIMEOUT2)
			conn.send("\nEnter your answer here: ")
			ans = input()
			if(ans == None):
				os._exit(0)			
			if(int(ans)!=minimum):
				conn.send("\nWrong.\n")
				os._exit(0)
			else:
				conn.send("\nCorrect.\n")			
 			if(i==149):
				flag = True
		if(flag == True):
			conn.send("\nCongratulations! The flag is: d4rk" + chr(123) + "pr0Gr4mM1ng_15_fUn" + chr(125) + "c0de\n")
	else:
		os._exit(0)
else:
	os._exit(0)






