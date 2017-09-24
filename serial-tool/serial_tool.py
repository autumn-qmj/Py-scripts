#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'serial tool'


__author__ = 'cc'

from ui.serial_ui import *
from port.serial_port import *
from Tkinter import *
from ttk import *


class Serial_tool(Serial_ui):

	def __init__(self, master = None):
		Serial_ui.__init__(self, master)
		self.update_port_list_ui()

	def serialport_list(self):
		portList = list(serial.tools.list_ports.comports())
		if(len(portList) <= 0):
			return None
		else:
			d = {}
			port = [list(x) for x in portList]
			for x in port:
				d[x[0]] = x[1]
			return d	

	def click_open(self):
		pass

	def click_refresh(self):
		self.update_port_list_ui()
				
	def update_port_list_ui(self):
		self.portListUI = self.serialport_list()
		if self.portListUI != None:
			portList = [x for x in self.portListUI]
		else:
			portList = []
			self.statusText.set('')
		self.comList.set(tuple(portList))

	def selectComPortList(self, event):
		self.statusText.set(self.portListUI[self.listbox.get(self.listbox.curselection())])

if __name__ == '__main__':
	root = Tk()
	root.title("serial tool")

	s=Serial_tool(master = root)

	root.mainloop()