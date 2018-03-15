#!/usr/bin/env python

import cv2
import sys
import caffe
#!/usr/bin/env python
import cv2
import os
import numpy
import math
import numpy as np
from os import walk
import xml.etree.ElementTree as ET
import sys
sys.path.append('/home/min/a/ee570/edge-boxes-with-python/')
import edge_boxes

def bb_intersection_over_union(boxA, boxB):
        # determine if the boxes don't overlap at all
        if (boxB[0] > boxA[2]) or (boxA[0] > boxB[2]) or (boxB[1] > boxA[3]) or (boxA[1] > boxB[3]):
                return 0

        # determine the (x, y)-coordinates of the intersection rectangle
        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])

        # compute the area of intersection rectangle
        interArea = (xB - xA + 1) * (yB - yA + 1)

        # compute the area of both the prediction and ground-truth rectangles
        boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
        boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

        # compute the intersection over union by taking the intersection
        # area and dividing it by the sum of prediction + ground-truth
        # areas - the interesection area
        iou = interArea / float(boxAArea + boxBArea - interArea)

        # return the intersection over union value
        return iou
#************************************************************************************************************************************







model = "./hw3-deploy.prototxt"
weights = "./hw3-weights.caffemodel"

caffe.set_mode_cpu()

net = caffe.Net(model, weights, caffe.TEST)

f = "./hw3-test-split.txt"
nnInputWidth = 32
nnInputHeight = 32
f = open(f, 'r')
total = 0
num = 0
w=[]
ka="/home/min/a/prachapu/ee570/hw3/"
while True:
	line = f.readline()
	if not line:
		break
	l = line.split()
	pa = l[0][2:]
	l[0] = ka + pa
#	print line, l
#	print l
	print(l[0])
	w=[]
	w.append(l[0])
	windows = edge_boxes.get_windows(w)
	windows = numpy.array(windows)
	image = cv2.imread(l[0])
#	cv2.imshow('image',image)
#	cv2.waitKey(0)
	#print windows
	prop_ctr=0
	best=-1
	result=[]
	store =[]
	for u in xrange(0,4):
		result.append(0)
		store.append([])
	for proposals in windows:
		for boxes in proposals:
			p=[]
			print"Proposal Number: ",prop_ctr
			p=boxes
	#		print p[1]
	#		print "hello"
        	        x1 = int(p[1])
               		y1 = int(p[0])
                	x2 = int(p[3])
                	y2 = int(p[2])	
			img = image[y1:y2,x1:x2]
			box = [x1, y1, x2, y2] 
			inputResImg = cv2.resize(img, (nnInputWidth, nnInputHeight), interpolation=cv2.INTER_CUBIC)
	        	transposedInputImg =inputResImg.transpose(2,0,1)
        		net.blobs['data'].data[...]=transposedInputImg
        		out = net.forward()
			max_value=0
        		max_iter=-1
       			total = total + 1
        		for y in out:
                		scores = out[y]
			#	print "SCORES:   ", scores
                		for x in range(len(scores[0])):
                        		k = scores[0][x]
                        		if k > max_value:
                                		max_value = k
                               			max_iter = x
			#	print "MAX:  ",max_value, " ITER: ",max_iter
                           	if max_iter== 4:
					continue
				else:
					if result[max_iter] <= max_value:
						result[max_iter] = max_value
						store[max_iter] = box
						best = prop_ctr

			prop_ctr=prop_ctr+1
	k=0
	da = 0
	s=""
	sa=0
	ans=0
	for ans in xrange(0,4):	
	
		if k < result[ans]:
			k = result[ans]
			da = ans
			sa = k
	if da ==0:
		s = "FOX"
	elif da==1:
		s= "BIKE"
	elif da==2:
		s= "ELEPHANT"
	elif da==3:
		s="CAR"
	else:
		s="INDETERMINANT"
	
	print "Best Proposal Id : ",best
	print "Best Proposal Score: ",sa
	print "Best Proposal Class: ",s
	if store[ans]==[]:
		cv2.imshow('origImage',image)
	else:
		xx1 = store[ans][0]
		yy1 = store[ans][1]
		xx2 = store[ans][2]
		yy2 = store[ans][3]
		cv2.rectangle(image, (xx1, yy1), (xx2, yy2), (0, 255, 0), 1)
		cv2.imshow('origImage', image)
	print "Press the space bar to procced to the next image: "
	cv2.waitKey(0)
	
		
			
