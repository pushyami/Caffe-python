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

datasetDir   = '/home/min/a/ee570/hw3-files/hw3-dataset'

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

imageDir = datasetDir + "/n02119789/"
imageFiles = []

for (dirpath, dirnames, filenames) in walk(imageDir):
        imageFiles.extend(filenames)
        break

if not os.path.exists("fox_pos"):
	os.makedirs("fox_pos")

if not os.path.exists("fox_neg"):
	os.makedirs("fox_neg")

imageFileNames = []
for i in xrange(0,len(imageFiles)):
	imageFileNames.append(imageDir + imageFiles[i]) #replace by a loop over all the images in that directory
windows = edge_boxes.get_windows(imageFileNames)
windows = numpy.array(windows)
count = 0
img_ctr = 0
box_ctr=0
neg_ctr = 0
pos_ctr = 0
path_pos = "/home/min/a/prachapu/ee570/hw3/fox_pos/"
path_neg = "/home/min/a/prachapu/ee570/hw3/fox_neg/"
for images in windows:
	box_ctr=0
	saved_pos = 0
	saved_neg = 0
	name = imageFileNames[count].split("/")[8].split(".")[0]	
	annotationFilename = datasetDir + "/annotation/n02119789/"+name+".xml"
	tree = ET.parse(annotationFilename)
	objs = tree.findall('object')
	numObjs = len(objs)
	img = cv2.imread(imageFileNames[count])
	for boxes in images:
		
		if saved_pos >= 5:
			break
		print "Image Num: ",img_ctr, " Box Counter: ",box_ctr
		images[box_ctr] = images[box_ctr].astype(float)
		l = []
		for index in boxes:	
			l.append(int(math.floor(index)))
		x1 = l[1]
		#print x1
		y1 = l[0]
		x2 = l[3]
		y2 = l[2]
		
		box = [x1, y1, x2, y2]
		max_iou = 0	
		for ix, obj in enumerate(objs):
			bbox = obj.find("bndbox")
			groundTruth_x1 = int(bbox.find("xmin").text)
			groundTruth_y1 = int(bbox.find("ymin").text)
			groundTruth_x2 = int(bbox.find("xmax").text)
			groundTruth_y2 = int(bbox.find("ymax").text)

			groundTruthBox = [groundTruth_x1, groundTruth_y1, groundTruth_x2, groundTruth_y2]
			iou = bb_intersection_over_union(box, groundTruthBox)
			if iou > max_iou:
				max_iou = iou
				
		if max_iou >=0.7:
			if saved_pos<5:
				s = "fox_img_pos_"+str(pos_ctr)+".jpg"
				pos_ctr=pos_ctr+1
				print "Saving in Pos_saved: ",s,"**************************************************************************************************************"
				cv2.imwrite(os.path.join(path_pos ,s), img[y1:y2, x1:x2])
				saved_pos = saved_pos + 1
		if max_iou < 0.4:
			if saved_neg <5:
				s = "fox_img_neg_"+str(neg_ctr)+".jpg"
				neg_ctr=neg_ctr+1
				print "Saving in Neg_saved: ",s,"****************************************************************************************************************"
				cv2.imwrite(os.path.join(path_neg ,s), img[y1:y2, x1:x2])
				saved_neg = saved_neg + 1
		box_ctr = box_ctr+1
	img_ctr=img_ctr+1	
	count = count + 1
		
imageDir = datasetDir + "/n02504458/"

imageFiles = []

for (dirpath, dirnames, filenames) in walk(imageDir):
        imageFiles.extend(filenames)
        break

if not os.path.exists("elephant_pos"):
        os.makedirs("elephant_pos")

if not os.path.exists("elephant_neg"):
        os.makedirs("elephant_neg")

imageFileNames = []
for i in xrange(0,len(imageFiles)):
        imageFileNames.append(imageDir + imageFiles[i]) #replace by a loop over all the images in that directory
windows = edge_boxes.get_windows(imageFileNames)
windows = numpy.array(windows)
print windows

count = 0
img_ctr = 0
box_ctr=0
neg_ctr = 0
pos_ctr = 0
path_pos = "/home/min/a/prachapu/ee570/hw3/elephant_pos/"
path_neg = "/home/min/a/prachapu/ee570/hw3/elephant_neg/"
for images in windows:
        box_ctr=0
        saved_pos = 0
        saved_neg = 0
        name = imageFileNames[count].split("/")[8].split(".")[0]
        annotationFilename = datasetDir + "/annotation/n02504458/"+name+".xml"
        tree = ET.parse(annotationFilename)
        objs = tree.findall('object')
        numObjs = len(objs)
        img = cv2.imread(imageFileNames[count])
        for boxes in images:

                if saved_pos >= 5:
                        break
                print "Image Num: ",img_ctr, " Box Counter: ",box_ctr
                images[box_ctr] = images[box_ctr].astype(float)
                l = []
                for index in boxes:
                        l.append(int(math.floor(index)))
                x1 = l[1]
                #print x1
                y1 = l[0]
                x2 = l[3]
                y2 = l[2]

                box = [x1, y1, x2, y2]
                max_iou = 0
                for ix, obj in enumerate(objs):
                        bbox = obj.find("bndbox")
                        groundTruth_x1 = int(bbox.find("xmin").text)
                        groundTruth_y1 = int(bbox.find("ymin").text)
                        groundTruth_x2 = int(bbox.find("xmax").text)
                        groundTruth_y2 = int(bbox.find("ymax").text)

			groundTruthBox = [groundTruth_x1, groundTruth_y1, groundTruth_x2, groundTruth_y2]
                        iou = bb_intersection_over_union(box, groundTruthBox)
                        if iou > max_iou:
                                max_iou = iou

                if max_iou >=0.7:
                        if saved_pos<5:
                                s = "elephant_img_pos_"+str(pos_ctr)+".jpg"
                                pos_ctr=pos_ctr+1
                                print "Saving in Pos_saved: ",s,"**************************************************************************************************************"
                                cv2.imwrite(os.path.join(path_pos ,s), img[y1:y2, x1:x2])
                                saved_pos = saved_pos + 1
                if max_iou < 0.4:
                        if saved_neg <5:
                                s = "elephant_img_neg_"+str(neg_ctr)+".jpg"
                                neg_ctr=neg_ctr+1
                                print "Saving in Neg_saved: ",s,"****************************************************************************************************************"
                                cv2.imwrite(os.path.join(path_neg ,s), img[y1:y2,x1:x2])
                                saved_neg = saved_neg + 1
                box_ctr = box_ctr+1
        img_ctr=img_ctr+1
        count = count + 1


imageDir = datasetDir + "/n03792782/"

imageFiles = []

for (dirpath, dirnames, filenames) in walk(imageDir):
        imageFiles.extend(filenames)
        break

if not os.path.exists("bike_pos"):
        os.makedirs("bike_pos")

if not os.path.exists("bike_neg"):
        os.makedirs("bike_neg")

imageFileNames = []
for i in xrange(0,len(imageFiles)):
        imageFileNames.append(imageDir + imageFiles[i]) #replace by a loop over all the images in that directory
windows = edge_boxes.get_windows(imageFileNames)
windows = numpy.array(windows)
count = 0
img_ctr = 0
box_ctr=0
neg_ctr = 0
pos_ctr = 0
path_pos = "/home/min/a/prachapu/ee570/hw3/bike_pos/"
path_neg = "/home/min/a/prachapu/ee570/hw3/bike_neg/"
for images in windows:
        box_ctr=0
        saved_pos = 0
        saved_neg = 0
        name = imageFileNames[count].split("/")[8].split(".")[0]
        annotationFilename = datasetDir + "/annotation/n03792782/"+name+".xml"
        tree = ET.parse(annotationFilename)
        objs = tree.findall('object')
        numObjs = len(objs)
        img = cv2.imread(imageFileNames[count])
        for boxes in images:

                if saved_pos >= 5:
			break
                print "Image Num: ",img_ctr, " Box Counter: ",box_ctr
                images[box_ctr] = images[box_ctr].astype(float)
                l = []
                for index in boxes:
                        l.append(int(math.floor(index)))
                x1 = l[1]
                #print x1
                y1 = l[0]
                x2 = l[3]
                y2 = l[2]

                box = [x1, y1, x2, y2]
                max_iou = 0
                for ix, obj in enumerate(objs):
                        bbox = obj.find("bndbox")
                        groundTruth_x1 = int(bbox.find("xmin").text)
                        groundTruth_y1 = int(bbox.find("ymin").text)
                        groundTruth_x2 = int(bbox.find("xmax").text)
                        groundTruth_y2 = int(bbox.find("ymax").text)

                        groundTruthBox = [groundTruth_x1, groundTruth_y1, groundTruth_x2, groundTruth_y2]
                        iou = bb_intersection_over_union(box, groundTruthBox)
                        if iou > max_iou:
                                max_iou = iou

                if max_iou >=0.7:
                        if saved_pos<5:
                                s = "bike_img_pos_"+str(pos_ctr)+".jpg"
                                pos_ctr=pos_ctr+1
                                print "Saving in Pos_saved: ",s,"**************************************************************************************************************"
                                cv2.imwrite(os.path.join(path_pos ,s), img[y1:y2, x1:x2])
                                saved_pos = saved_pos + 1
                if max_iou < 0.4:
                        if saved_neg <5:
                                s = "bike_img_neg_"+str(neg_ctr)+".jpg"
                                neg_ctr=neg_ctr+1
                                print "Saving in Neg_saved: ",s,"****************************************************************************************************************"
                                cv2.imwrite(os.path.join(path_neg ,s), img[y1:y2,x1:x2])
                                saved_neg = saved_neg + 1
                box_ctr = box_ctr+1
        img_ctr=img_ctr+1
        count = count + 1

imageDir = datasetDir + "/n04037443/"

imageFiles = []

for (dirpath, dirnames, filenames) in walk(imageDir):
        imageFiles.extend(filenames)
        break

if not os.path.exists("car_pos"):
        os.makedirs("car_pos")

if not os.path.exists("car_neg"):
        os.makedirs("car_neg")

imageFileNames = []
for i in xrange(0,len(imageFiles)):
        imageFileNames.append(imageDir + imageFiles[i]) #replace by a loop over all the images in that directory
windows = edge_boxes.get_windows(imageFileNames)
windows = numpy.array(windows)
count = 0
img_ctr = 0
box_ctr=0
neg_ctr = 0
pos_ctr = 0
path_pos = "/home/min/a/prachapu/ee570/hw3/car_pos/"
path_neg = "/home/min/a/prachapu/ee570/hw3/car_neg/"
for images in windows:
        box_ctr=0
        saved_pos = 0
        saved_neg = 0
        name = imageFileNames[count].split("/")[8].split(".")[0]
        annotationFilename = datasetDir + "/annotation/n04037443/"+name+".xml"
        tree = ET.parse(annotationFilename)
        objs = tree.findall('object')
        numObjs = len(objs)
        img = cv2.imread(imageFileNames[count])
        for boxes in images:

                if saved_pos >= 5:
                        break
                print "Image Num: ",img_ctr, " Box Counter: ",box_ctr
                images[box_ctr] = images[box_ctr].astype(float)
                l = []
                for index in boxes:
                        l.append(int(math.floor(index)))
                x1 = l[1]
                #print x1
                y1 = l[0]
                x2 = l[3]
                y2 = l[2]

                box = [x1, y1, x2, y2]
                max_iou = 0
		for ix, obj in enumerate(objs):
                        bbox = obj.find("bndbox")
                        groundTruth_x1 = int(bbox.find("xmin").text)
                        groundTruth_y1 = int(bbox.find("ymin").text)
                        groundTruth_x2 = int(bbox.find("xmax").text)
                        groundTruth_y2 = int(bbox.find("ymax").text)

                        groundTruthBox = [groundTruth_x1, groundTruth_y1, groundTruth_x2, groundTruth_y2]
                        iou = bb_intersection_over_union(box, groundTruthBox)
                        if iou > max_iou:
                                max_iou = iou

                if max_iou >=0.7:
                        if saved_pos<5:
                                s = "car_img_pos_"+str(pos_ctr)+".jpg"
                                pos_ctr=pos_ctr+1
                                print "Saving in Pos_saved: ",s,"**************************************************************************************************************"
                                cv2.imwrite(os.path.join(path_pos ,s), img[y1:y2, x1:x2])
                                saved_pos = saved_pos + 1
                if max_iou < 0.4:
                        if saved_neg <5:
                                s = "car_img_neg_"+str(neg_ctr)+".jpg"
                                neg_ctr=neg_ctr+1
                                print "Saving in Neg_saved: ",s,"****************************************************************************************************************"
                                cv2.imwrite(os.path.join(path_neg ,s), img[y1:y2,x1:x2])
                                saved_neg = saved_neg + 1
                box_ctr = box_ctr+1
        img_ctr=img_ctr+1
        count = count + 1

