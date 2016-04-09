import smbus
import thread


class I2C(object):

	def __init__(self):

		print "init"

		self.address = 0x5
		self.bus = smbus.SMBus(1)


	def write(self, x):

	    data = x

	    self.bus.write_byte_data(address, data, 0)


	def fixData(self, x):
		
		#method to make data a 6 byte string
		data = x


		if data > 0: 
			#data is postive

			if data < 10.00:
				#data is 4 characters
				data = str(data)
				data = data + "00" 
				return data
				
			elif data > 10.00:
				#data is 5 characters
				data = str(data)
				data = data + "0"
				return data

			else:
				print "something went wrong with your data"
				#raise dataError

		elif data < 0:
			#data is negative

			if data < 10.00:
				#data is 5 characters
				data = str(data)
				data = data + "0"
				return data

			elif data > 10.00:
				#data is already 6 characters
				data = str(data)
				return data

			else:
				print "something went wrong with your data"
				#raise dataError

		elif data == -1000:
			#no angle is found and angle already has 6 digits
			data = str(data)
			return data

		else:
			print "something with your data is seriously messed up"
			#raise dataError



def startServer():
		
	putData(-1000)

	global i2c
	i2c = I2C()

	thread.start_new_thread(run, ())
	print "server started"



def run():

	while(1):

		fixedData = i2c.fixData(angle)
		print fixedData
		#ic2.write(fixedData)



def putData(x):

	global angle

	angle = x


