#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'serial tool'


__author__ = 'cc'

from ui.serial_ui import *
from port.serial_port import *
from Tkinter import *
from ttk import *
import threading


class Serial_tool(Serial_ui):

	def __init__(self, master = None):
		Serial_ui.__init__(self, master)
		self.port = None
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
		if self.listbox.curselection() == ():
			pass
		else:
			self.port = self.listbox.get(self.listbox.curselection())
			if self.openText.get() == 'open':
				self.serialDev = Serial_port(self.port, self.baudrate.get(), BytesizeList[self.bytesize.get()],
								ParityList[self.parity.get()], StopbitsList[self.stopbits.get()], xonxoff = FlowCtrlList[self.flowctrl.get()],
								rtscts = DtrrtsList[self.rts.get()], dsrdtr = DtrrtsList[self.dtr.get()])
				if self.serialDev.serialport_open():
					self.update_status_text(self.port + ' open successfully')
					self.openText.set('close')
					self.update_recv_text()
				else:
					self.update_status_text(self.port + ' open Failed, Please check the connection')
			else:
				self.openText.set('open')
				self.update_status_text(self.port + ' closed')
				self.serialDev.serialport_close()
		
	def click_refresh(self):
		self.update_port_list_ui()
				
	def update_port_list_ui(self):
		self.portListUI = self.serialport_list()
		if self.portListUI != None:
			portList = [x for x in self.portListUI]
		else:
			portList = []
			self.update_status_text('')
		if self.port != None:
			if self.port not in portList:
				self.openText.set('open')
				self.update_status_text(self.port + ' removed')
		self.comList.set(tuple(portList))

	def selectComPortList(self, event):
		if self.listbox.curselection() != ():
			self.update_status_text(self.portListUI[self.listbox.get(self.listbox.curselection())])

	def update_status_text(self, str):
		self.statusText.set(str)

	def update_recv_text(self):
		self.serialDev.serialport_read()
		if self.serialDev.recvData:
			self.recvText.insert(END, self.serialDev.recvData)
			self.recvText.see(END)#make sure the slider always align with bottom
			self.serialDev.recvData = None
		self.after(10, self.update_recv_text)

if __name__ == '__main__':
	root = Tk()
	root.title("serial tool")

	s=Serial_tool(master = root)

	root.mainloop()