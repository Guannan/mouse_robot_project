#!/usr/bin/env python

import os
import glob
from SimpleCV import *
from time import sleep

path = os.getcwd()
extension = '*.jpg'

imgs = list() #load up an image list
directory = os.path.join(path, extension)
images = glob.glob(directory)

for image in images:
   	cur_image = Image(image)

	facelayer = DrawingLayer((cur_image.width, cur_image.height))
	facebox_dim = (80,80)

	face_feature = HaarCascade('face.xml')
	# face_feature = HaarCascade('haarcascade_frontalface_alt2.xml')
	# face_feature = HaarCascade('haarcascade_profileface.xml')
	found_faces = cur_image.findHaarFeatures(face_feature)

	if found_faces:
		for face in found_faces:
			face_coord = face.coordinates()
			print 'Face location at: ' + str(face.coordinates())
			center_point = (face_coord[0], face_coord[1])
			facebox = facelayer.centeredRectangle(center_point, facebox_dim)
			cur_image.addDrawingLayer(facelayer)
			cur_image.applyLayers()

		   	cur_image.show()
		   	time.sleep(5)

