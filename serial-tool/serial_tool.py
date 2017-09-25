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
		if self.openText.get() == 'open':
			if self.listbox.curselection() == ():
				pass
			else:
				port = self.listbox.get(self.listbox.curselection())
				print self.flowctrl.get()
				print FlowCtrlList[self.flowctrl.get()]
				self.serialDev = Serial_port(port, self.baudrate.get(), BytesizeList[self.bytesize.get()],
								ParityList[self.parity.get()], StopbitsList[self.stopbits.get()], xonxoff = FlowCtrlList[self.flowctrl.get()],
								rtscts = DtrrtsList[self.rts.get()], dsrdtr = DtrrtsList[self.dtr.get()])
				if self.serialDev.serialport_open():
					self.update_status_text(port + ' open successfully')
					self.openText.set('close')
				else:
					self.update_status_text(port + ' open Failed, Please check the connection')
		else:
			self.openText.set('open')
			self.update_status_text(port + ' closed')
			self.serialport_close()
		

	def click_refresh(self):
		self.update_port_list_ui()
				
	def update_port_list_ui(self):
		self.portListUI = self.serialport_list()
		if self.portListUI != None:
			portList = [x for x in self.portListUI]
		else:
			portList = []
			self.update_status_text('')
		self.comList.set(tuple(portList))

	def selectComPortList(self, event):
		if self.listbox.curselection() != ():
			self.update_status_text(self.portListUI[self.listbox.get(self.listbox.curselection())])

	def update_status_text(self, str):
		self.statusText.set(str)


if __name__ == '__main__':
	root = Tk()
	root.title("serial tool")

	s=Serial_tool(master = root)

	root.mainloop()