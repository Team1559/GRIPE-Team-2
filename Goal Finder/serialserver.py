
import serial
import sys
import thread
import time


#lock = thread.allocate_lock()


class SerialServer(object):

	def __init__(self):

		print "init"

		global port
		port = serial.Serial("/dev/ttyAMA0", baudrate = 115200, timeout = 0.01)


	def send(self, x):

		err = x
		#angle = y
		#distance = z

		port.write(err+"t")



def startServer():

	putData(-321)

	global s
	s = SerialServer()

	thread.start_new_thread(run, ())
	print "server started"



def run():

	while(1):

		message = port.read()
		#print error

		if message == "s":

			print error
			s.send(str(error))

	print "bye bye"



def putData(x):

	global error
	global distance
	global angle

	error = x
	#angle = y
	#distance = z

