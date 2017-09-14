#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'serial port status'


__author__ = 'cc'

import serial
import serial.tools.list_ports

port_list = list(serial.tools.list_ports.comports())

if(len(port_list) < 0):
	print('serial port not avaliable')
else:
	port_name = [list(x)[0] for x in port_list]
	print(port_name)


class serial_port(serial):
	"""docstring for serial_port"""
	def __init__(self, arg):
		super(serial_port, self).__init__()
		self.arg = arg
		