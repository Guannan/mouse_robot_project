#!/usr/bin/env python

from SimpleCV import Camera, Display, DrawingLayer, Color
from time import sleep, time

myCamera = Camera(prop_set={'width':320, 'height': 240})
myDisplay = Display(resolution=(320, 240))

while not myDisplay.isDone():
	frame = myCamera.getImage()
	frame_flipud = frame.rotate(180)
	
	start_time = time()
	faces = frame_flipud.findHaarFeatures('face')
	end_time = time()
	elapsed_time = end_time - start_time
	print 'Elapsed time : ' + str(elapsed_time)

	facelayer = DrawingLayer((frame_flipud.width, frame_flipud.height))
	facebox_dim = (40,40)  # draws a 40 by 40 pixel dimensioned box

#	if faces:
		#for face in faces:
			#face_coord = face.coordinates ()
			#center_point = (face_coord[0], face_coord[1])
			#facebox = facelayer.centeredRectangle(center_point, facebox_dim, color=Color.RED)
			#frame_flipud.addDrawingLayer(facelayer)  # draws box around center of detected face
			#frame_flipud.applyLayers()
			#print "Face at: " + str(face.coordinates())
	#else:
		#print "No faces detected."
	frame_flipud.save(myDisplay)
	sleep(0.1)

