import xml.etree.ElementTree as ET
#from datetime import datetime as DT

class xmlReader:
	tree = ET.parse("file1.xml")	#parses into ElementTree wrapper class
	print('tree: ',tree)
	print('dir: ',dir(ET))
	# this element holds the phonebook entries
	container = tree.find("entries")
	print('container type: ',type(container))
	#print('root: ',tree.getroot())
	data = []
	for elem in container:
		key = elem.findtext("number")
		#print('key: ',key)
		data.append((key, elem))
		#print('data: ',data)

	data.sort()
	#print('sort: ',data)
	# insert the last item from each tuple
	container[:] = [item[-1] for item in data]
	print("\n")
	outputName = input("Enter O/P file name : ")
	if outputName:
		tree.write(outputName +".xml")
	else:
		print("\n")
		print("Enter a file name!\n")
		outputName = input("Enter O/P file name : ")
		tree.write(outputName +".xml")