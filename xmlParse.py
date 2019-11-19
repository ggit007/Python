import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM

class xmlParse:

	file = open("file1.xml")
	#print('file1: '+file.read())
	#openFile
	parse = ET.parse("L.xml")
	root = parse.getroot()
	print('root: ',root)
	
	nameTag = []
	for child in root.iter('number'):	#iterating to each child
		#print('child: ',child.text)
		nameTag.append(child.text)
		#print('nameTag: ',nameTag)
		nameTag.sort()
		#print('nameTag: ',nameTag)
		
	xmlBody = '<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n'+'<Package xmlns=\"http://soap.sforce.com/2006/04/metadata\">'
    
	#print(xmlBody)
	for name in nameTag:
		xmlBody +='<members>' + '*' + '</members>'
		xmlBody +='<name>' + name + '</name>'		
		
	xmlBody += '<version>46.0</version>'
	xmlBody += '</Package>'
	print(xmlBody)
	
	fileName = input('Output file name: ')
	if fileName:
		xml = DOM.parseString(xmlBody)
		prettyXML = xml.toprettyxml()
		createXML = open(fileName+'.xml',"w")
		createXML.write(prettyXML)
	elif not fileName:
		print("\n")
		print('Give a file name !')
		createXML = open(fileName+'.xml',"w")
		createXML.write(xmlBody)
	else:
		input('Do you wish to overwrite the existing file ? y or n: ')
		if y:
			createXML = open(fileName+'.xml',"w")
			createXML.write(xmlBody)
		
	
	