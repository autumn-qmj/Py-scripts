#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'serial tool'


__author__ = 'cc'

from ui.serial_ui import *
from port.serial_port import *
from Tkinter import *
from ttk import *
import threading

supportInputChar = {'\r','\n','Q','A','Z','W','S','X','E','D','C','R','F','V','T','G','B','Y','H','N','U','J','M','I','K','O','L','P','q','a','z','w','s','x','e','d','c','r','f','v','t','g','b','y','h','n','u','j','m','i','k','l','o','p','0','9','8','7','6','5','4','3','2','1'}

class Serial_tool(Serial_ui):

	def __init__(self, master = None):
		Serial_ui.__init__(self, master)
		self.port = None
		self.portListUI = {}

		self.update_port_list_ui()
		self.check_port_status_backend()
		self.sendText = None

	def serialport_list(self):
		portList = list(serial.tools.list_ports.comports())
		if(len(portList) <= 0):
			return None
		else:
			port = [list(x) for x in portList]
			self.portListUI = {}
			for x in port:
				self.portListUI[x[0]] = x[1]
			return  [x for x in self.portListUI]

	def click_open(self):
		if self.listbox.curselection() == ():
			pass
		else:
			if self.port != None:
				self.serialDev.serialport_close()
				self.port = None

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
				self.port = None

	def click_send(self):
		pass

	def click_refresh(self):
		self.update_port_list_ui()
				
	def update_port_list_ui(self):
		pl = self.serialport_list()
		if pl != None:
			self.comList.set(tuple(pl))

	def check_port_status_backend(self):
		pl1 = self.serialport_list()
		if self.port != None:
			if self.port not in pl1:
				self.serialDev.serialport_close()
				self.comList.set(tuple(pl1))
				self.openText.set('open')
				self.update_status_text(self.port + ' removed')
				self.port = None
		self.after(50, self.check_port_status_backend)

	def selectComPortList(self, event):
		if self.listbox.curselection() != ():
			self.update_status_text(self.portListUI[self.listbox.get(self.listbox.curselection())])
			if self.listbox.get(self.listbox.curselection()) != self.port:
				self.openText.set('open')
			else:
				self.openText.set('close')

	def update_status_text(self, str):
		self.statusText.set(str)

	def update_recv_text(self):
		self.serialDev.serialport_read()
		if self.serialDev.recvData:
			self.recvText.insert(END, self.serialDev.recvData)
			self.recvText.see(END)#make sure the slider always align with bottom
			self.serialDev.recvData = None
		self.after(10, self.update_recv_text)

	def releaseKey(self, event):
		if event.char in supportInputChar:
			if self.port:
		 		self.serialDev.serialport_write(event.char, False)

	def pressKey(self, event):
		pass

if __name__ == '__main__':
	root = Tk()
	root.title("serial tool")
	# root.columnconfigure(0, weight=1)
	# root.rowconfigure(0, weight=1)
	# root.rowconfigure(1, weight=1)
	# root.rowconfigure(2, weight=1)
	s=Serial_tool(master = root)

	root.mainloop()