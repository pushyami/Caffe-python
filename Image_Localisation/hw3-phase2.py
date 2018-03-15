from os import walk
import sys
imageFiles = []
f = open("new_data.txt","a")
imageDir0 = "fox_pos"
imageDir1 = "bike_pos"
imageDir2 = "elephant_pos"
imageDir3 = "car_pos"
fullname="/home/min/a/prachapu/ee570/hw3/"
imageFile=[]
count = 0
for (dirpath, dirnames, filenames) in walk(imageDir0):
	imageFile.extend(filenames)
	
	break
for filenames in imageFile:
	if count <600:
		f.write(fullname+"fox_pos/"+filenames+" 0\n")
	else:
		break
	count = count +1
imageFile=[]
count =0
for (dirpath, dirnames, filenames) in walk(imageDir1):
	imageFile.extend(filenames)
	break
for filenames in imageFile:
	#print filenames	
	if count <600:
		f.write(fullname+"bike_pos/"+filenames+" 1\n")
	else:
		break
	count = count +1
imageFile=[]
count = 0
for (dirpath, dirnames, filenames) in walk(imageDir2):
	imageFile.extend(filenames)
	break
for filenames in imageFile:
	#print filenames	
	if count <600:
		f.write(fullname+"elephant_pos/"+filenames+" 2\n")
	else:
		break
	count = count +1
imageFile=[]
count = 0
for (dirpath, dirnames, filenames) in walk(imageDir3):
	imageFile.extend(filenames)
	break
for filenames in imageFile:
	#print filenames	
	if count <600:
		f.write(fullname+"car_pos/"+filenames+" 3\n")
	else:
		break
	count = count +1

##############################################

imageDir0 = "fox_neg"
imageDir1 = "bike_neg"
imageDir2 = "elephant_neg"
imageDir3 = "car_neg"
imageFile=[]
for (dirpath, dirnames, filenames) in walk(imageDir0):
	imageFile.extend(filenames)
	
	break
count=0
for filenames in imageFile:
	if count <150:
		f.write(fullname+"fox_neg/"+filenames+" 4\n")
	else:
		break
	count = count +1
imageFile=[]
count =0
for (dirpath, dirnames, filenames) in walk(imageDir1):
	imageFile.extend(filenames)
	break
for filenames in imageFile:
	#print filenames	
	if count <150:
		f.write(fullname+"bike_neg/"+filenames+" 4\n")
	else:
		break
	count = count +1
imageFile=[]
count = 0
for (dirpath, dirnames, filenames) in walk(imageDir2):
	imageFile.extend(filenames)
	break
for filenames in imageFile:
	#print filenames	
	if count <150:
		f.write(fullname+"elephant_neg/"+filenames+" 4\n")
	else:
		break
	count = count +1
imageFile=[]
count = 0
for (dirpath, dirnames, filenames) in walk(imageDir3):
	imageFile.extend(filenames)
	break
for filenames in imageFile:
	#print filenames	
	if count <150:
		f.write(fullname+"car_neg/"+filenames+" 4\n")
	else:
		break
	count = count +1






