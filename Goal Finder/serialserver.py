#!/usr/bin/python

import serial
import sys
import thread
import time
#import logging
#logging.basicConfig(level=logging.debug)
#import sys


#lock = thread.allocate_lock()


class SerialServer(object):

	def __init__(self):

		print "init"

		global port
		port = serial.Serial("/dev/ttyAMA0", baudrate = 115200, timeout = 0.01)


	def send(self, x):

		#err = x
		ang = x
		#dist = z
		#print ang
		port.write(ang+"t")
		#print ang



def startServer():

	putData(-100)

	global s
	s = SerialServer()

	thread.start_new_thread(run, ())
	print "server started"



def run():

	while(1):

		message = port.read()
		#print angle

		if message == "s":
                        #print angle
			#sys.stderrr.write(angle)
			s.send(str(angle))

	print "bye bye"



def putData(x):

	global error
	global distance
	global angle

	#error = x
	angle = x
	#distance = z

