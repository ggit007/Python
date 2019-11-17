class pythonTesting:

	x = ['b','a','c','d']
	#x.append(('c','d'))
	x[:] = [item[0] for item in x]
	print('x: ',x)