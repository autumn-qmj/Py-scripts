#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'serial port class'


__author__ = 'cc'

import serial
import serial.tools.list_ports
import binascii
import logging


def serialport_list():

	port_list = list(serial.tools.list_ports.comports())

	if(len(port_list) <= 0):
		print('serial port not avaliable')
		return None
	else:
		port = [list(x) for x in port_list]
		print('Total com ports %d:\n'%len(port))
	return port	

def serialport_Log():
	if s.recvData:
		print s.recvData
		s.recvData = None

class serial_port(object):
	"""docstring for serial_port"""
	def __init__(self, port=None, baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
		timeout=None, xonxoff=False, rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None):
		self.port = port
		self.baudrate = baudrate
		self.bytesize = bytesize
		self.parity = parity
		self.stopbits = stopbits
		self.timeout = timeout
		self.xonxoff = xonxoff
		self.rtscts = rtscts
		self.write_timeout = write_timeout
		self.dsrdtr = dsrdtr
		self.inter_byte_timeout = inter_byte_timeout
		self.device = None

	def serialport_open(self):
		self.device = serial.Serial()
		self.device.port = self.port
		self.device.baudrate = self.baudrate
		self.device.bytesize = self.bytesize
		self.device.parity = self.parity
		self.device.stopbits = self.stopbits
		self.device.timeout = self.timeout
		self.device.xonxoff = self.xonxoff
		self.device.rtscts = self.rtscts
		self.device.write_timeout = self.write_timeout
		self.device.dsrdtr = self.dsrdtr
		self.device.inter_byte_timeout = self.inter_byte_timeout
		try:
			self.device.open()
			if self.device.isOpen():
				self.alive = True
		except IOError as e:
			self.alive = False
			logging.error(e)
		
	def serialport_close(self):
		if self.device.isOpen():
			self.alive = False			
			self.device.close()

	def serialport_read(self):
		while self.alive:
			try:
				number = self.device.inWaiting()
				if number:
					self.recvData = self.device.readline(number)
					print self.recvData
			except IOError as e:
				logging.error(e)

	def serialport_write(self, data, isHex):
		if self.alive:
			if isHex:
				data = binascii.unhexlify(data)
			self.device.write(data)

if __name__ == '__main__':
	import threading

	port_list=serialport_list()
	if port_list != None:
		print('select port form list:\n%s'%port_list)
		port = raw_input()
		s=serial_port(port)
		s.serialport_open()
		serialRead = threading.Thread(target = s.serialport_read)
		serialPortLog = threading.Thread(target = serialport_Log)
		serialRead.setDaemon(True)
		serialRead.start()
		serialRead.join()
		#s.serialport_close()
