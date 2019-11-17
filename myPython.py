class myPython:			

	import datetime as dt	
	import random as rn
	from math import pi,factorial as fac
	import json as j
	import os
	import io
	#import salesforce as sfdc
	#from math import *
	
	print('My Python Learning !')
	
	
	if 5 < 2:
		print("Five is not greater than two!");
	elif 5 > 2:
		print("Five is greater than two!");
		print("Naughty")
		
	x = 1234
	print('Number '+str(x))
	
	x, y, z = "Orange", "Banana", "Cherry"
	print(x)
	print(y)
	print(z)
	
	x = y = z = "Orange"
	print(x)
	print(y)
	print(z)
	
	global e	#for instance variable use global
	e = dt.datetime.now()
	
	global u
	u = '123987'
	#print(x)
	
	def customFunction():
		#global u
		#u = 'global'
		u = 'random'
		#x = dt.datetime.now()
		print('Date: ',e,'printed')
		print('u: '+u)
		
	customFunction()
	
	print('u:~ '+u)
	
	x = [1,3,5,7,9]
	#x = 6
	print('range:',range(len(x)))
	
	#for i in range(len(x)):
	for i in range(1,7):
		print('Output',i)
		
	if bool():
		print('bool1: ','False')
	if bool(1):
		print('bool2: ','True')
		
	x = rn.randrange(10e6,20e6)
	print('Random:',x)
	
	print('pi: ',pi) 
	print('factorial: ',fac(6))
	
	g = 'Gaurav.com'
	print('g1: ',g[2])
	print('g2: ',g[2:5])
	print('g3: ',g[-4:-1])
	
	thisdict =	{
	  "brand": "Ford",
	  "model": "Mustang",
	  "year": 1964
	}
	for x,y in thisdict.items():
		print(x,':',y)
		
	thisdict =	{
	  "brand": "Ford",
	  "model": "Mustang",
	  "year": 1964
	}
	for x,y in thisdict.items():
		print(x)
	
	thisdict =	{
	  "brand": "Ford",
	  "model": "Mustang",
	  "year": 1964
	}
	for x,y in thisdict.items():
		print(y)
		
	def showCountry(country = 'India'):
		print('My Country is',country)
		
	showCountry()
	showCountry('US')
	
	x = ["A","B","C"]
	x.pop(2)
	print(x)
	
	x = ["A","B","C"]
	x.remove("A")
	print(x)
	
	tuple = 'kjhskdjksj'
	myIter = iter(tuple)
	print('iter: ',next(myIter))
	print('iter: ',next(myIter))
	
	for k in tuple:
		print('k: ',k)
		
	def function():
		x = 240
		def func():
			print('func: ',x)
		func()	
	function()
	
	x = 'ty'
	#print('Dir: ',dir(x))
	
	x = dt.datetime(2018, 6, 1)

	print(x.strftime("%c"))
	
	x =  '{ "name":"John", "age":30, "city":"New York"}'
	print('serial: ',j.loads(x)["age"])
	
	x = {"name":"John", "age":30, "city":"New York"}
	print('deserial:\n',j.dumps(x, indent = 3))
	
	#name = input('Please enter name: ')
	#print('Entered name is:',name)
	
	#f = open("demofile2.txt", "w")
	#f.write("Woops! I have deleted the content!")
	#f.close()	
	#print(f.read())
	
	if os.path.exists("demofile2.txt"):
		os.remove("demofile2.txt")
	else:
		print('no such file found!')
	#sf = dir(dt.datetime.now())
	#print('OS: ',sf)
	
	sf = dt.datetime.now()
	print(sf)
	
	y = dir(io.__file__)
	print('io: ',y)