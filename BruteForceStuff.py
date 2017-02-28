#Python 2

def Sha1_Brute_With_Names(reqdsha1,filename):
	import hashlib
	f=open(filename,'r')
	s=f.readlines()
	for i in range(len(s)):
		s[i]=s[i].strip()
		s[i]=s[i].title()
		#for changing the first letter to Uppercase
		eachpwd = s[i] + " Snow"
		sha_1 = hashlib.sha1()
		sha_1.update(eachpwd)
		finalhash = sha_1.hexdigest()
		if(finalhash==reqdsha1):
			print ("Name: " + eachpwd)

def Sha1_Brute_With_All_Word_Combinations(reqdsha1):
	import hashlib
	import itertools
	import string
	upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lower="abcdefghijklmnopqrstuvwxyz"
	for i in upper:
		#for first letter to be capital.
		for word in itertools.product(lower, repeat=7):
			#change repeat value to change the number characters you want to brute for.
			test=(i+''.join(word)+' Snow')
			sha_1=hashlib.sha1()
			sha_1.update(test)
			comp=sha_1.hexdigest()
			if comp==reqdsha1:
				print ("This is it: " + test)
				exit(0)

def Brute_Stuff_On_Terminal_Interactively():	
	import subprocess
	import itertools
	import string
	import pexpect
	import time
	import os,sys
	chars = '0123456789'
	L=[]
	for words in itertools.product(chars, repeat=5):
		L.append('1'+ ''.join(words))
		test=pexpect.spawn('openssl rsa -in HackIM.key -out answer.key')
		#time.sleep(1)
		test.logfile=sys.stdout
		test.expect(":")
		#time.sleep(1)
		test.send(('1'+ ''.join(words)) + '\n')
		test.logfile=sys.stdout
		test.expect(":")
		#test.interact()
		#openssl rsautl -decrypt -in message.new -inkey HackIM.key 

def Brute_Web_Stuff():
	from selenium.webdriver.common.keys import Keys
	from selenium import webdriver
	import time 	
	browser = webdriver.Firefox()
	browser.get('https://felicity.iiit.ac.in/contest/extra/fastandfurious/')
	while True:
		ansbox = browser.find_element_by_xpath("//input[@name='ques_ans']")
		sub = browser.find_element_by_xpath("//input[@type='submit']")
		content = browser.page_source
		start_index = content.find('Solve: (')
		end_index = content.find(' </p>',start_index+8)
		equation = content[start_index+8:end_index-1]
		equation = equation.replace(" ","")
		print equation
		answer = eval(equation)
		print answer
		ansbox.send_keys(answer)
		sub.click()
		time.sleep(1)

def Brute_With_Requests(url):
	import requests
	import threading
	def run(i):
		s = requests.Session()
		while True:
			data={'username': 'Admin', 'password': 'b', 'hash': '0', 'filename': '%d/../flag.php' % i, 'secret_password': 'b'}
			r = s.post(url, data)
			if len(r.text) != 5514:
				print r.text
				exit()
			i += len(ts)
	ts = []
	for i in range(20):
		t = threading.Thread(target=run, args=(i,))
		ts.append(t)
		t.start()

	for t in ts:
		t.join()
