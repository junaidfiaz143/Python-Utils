from xml.dom import minidom
from xml.etree import ElementTree as et
import os
import re

lc = "+"

def update_xml(path, num, lc):
	tree = et.parse(path)

	# tree.find('.//folder').text = 'data_object_detection_api'
	# tree.find('.//name').text = "not-pistol"
	print("Loading..." + lc, end="\r")

	if num[:5] == "armas":
		tree.find('.//filename').text = num+'.jpg'
		# tree.find('.//path').text = 'C:\\Users\\junaid\\Desktop\\CNN notebooks\\rename xml\\test\\'+num+'.jpg'
		tree.write(path)

path = 'C:\\Users\\junaid\\Desktop\\(pistol)-(not-pistol)\\2class_gun_no_guns_data\\test\\'

os.chdir(path)

for filename in os.listdir('.'):
	if filename.endswith(".xml"):
#         print(os.path.join(path, filename))
#         print(re.findall(r'\d+', filename)[0])
#         print(filename.split('.')[0])
		if lc == "+":
			lc = "-"
		else:
			lc = "+"
		update_xml(os.path.join(path, filename), filename.split('.')[0], lc)

print("\nDONE Updating XML.")