#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'serial tool UI'


__author__ = 'cc'

from Tkinter import *
from ttk import *

ConfigurationLabel = ['baudrate', 'bytesize', 'parity', 'stopbits', 'xonxoff', 'rts', 'dtr']
BaudrateList = [256000, 128000, 115200, 57600, 56000, 38400, 19200, 14400, 9600, 4800, 2400, 1200, 600, 300]
BytesizeList = [5, 6, 7, 8]
ParityList = ['None', 'Odd', 'Even', 'Mark', 'Space']
StopbitsList = ['1', '1.5', '2']
FlowCtrlList= ['None', 'Software']
DtrrtsList = ['Disable', 'Enable']
class serial_ui(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.pack(fill=BOTH, expand = True)

		
		#send button
		self.sendText = StringVar()
		entry = Entry(self, width = 20, textvariable = self.sendText).grid(column=2, row=1)
		buttonSend = Button(self, text='send', command = self.click_send).grid(column=4, row=1)
		
		for index, l in enumerate(ConfigurationLabel):
			Label(self, text=l).grid(column=0, row=2+index, sticky = 'w')

		#refresh button
		buttonRefresh = Button(self, text='refresh', command = self.click_refresh).grid(column=0, row=1)

		#open button
		self.openText = StringVar()
		self.openText.set('open')
		buttonOpen = Button(self, textvariable=self.openText, command = self.click_open).grid(column=1, row=1)

		#baudrate combobox
		self.baudrate = Combobox(self, values = BaudrateList, state = 'readonly', width = 10)
		self.baudrate.grid(column=1, row=2)
		self.baudrate.current(2)
		#bytesize combobox
		self.bytesize = Combobox(self, values = BytesizeList, state = 'readonly', width = 10)
		self.bytesize.grid(column=1, row=3)
		self.bytesize.current(3)
		#parity combobox
		self.parity = Combobox(self, values = ParityList, state = 'readonly', width = 10)
		self.parity.grid(column=1, row=4)
		self.parity.current(0)
		#stopbits combobox
		self.stopbits = Combobox(self, values = StopbitsList, state = 'readonly', width = 10)
		self.stopbits.grid(column=1, row=5)
		self.stopbits.current(0)
		#flow control combobox
		self.stopbits = Combobox(self, values = FlowCtrlList, state = 'readonly', width = 10)
		self.stopbits.grid(column=1, row=6)
		self.stopbits.current(0)
		#rts checkbutton
		self.rts = Combobox(self, values = DtrrtsList, state = 'readonly', width = 10)
		self.rts.grid(column=1, row=7)
		self.rts.current(0)
		#dtr checkbutton
		self.dtr = Combobox(self, values = DtrrtsList, state = 'readonly', width = 10)
		self.dtr.grid(column=1, row=8)
		self.dtr.current(0)
		

	def click_open(self):
		if self.openText.get() == 'open':
			self.openText.set('close')
		else:
			self.openText.set('open')

	def click_send(self):
		pass

	def click_refresh(self):
		pass


if __name__ == '__main__':
	root = Tk()
	root.title("serial tool")

	serial_ui(root)

	root.mainloop()