#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'serial tool UI'


__author__ = 'cc'

from Tkinter import *
from ttk import *

BaudrateList = [115200, 9600]

class serial_ui(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.pack(fill=BOTH, expand = True)

		#open button
		self.openText = StringVar()
		self.openText.set('open')
		buttonOpen = Button(self, textvariable=self.openText, command = self.click_open).grid(column=0, row=0)
		#send button
		self.sendText = StringVar()
		text = StringVar()
		entry = Entry(self, width = 20, textvariable = self.sendText).grid(column=0, row=1)
		buttonSend = Button(self, text='send', command = self.click_send).grid(column=4, row=1)
		#baudrate combobox
		baudrate = Combobox(self, values = BaudrateList, state = 'readonly').grid(column=0, row=2).current(0)


	def click_open(self):
		if self.openText.get() == 'open':
			self.openText.set('close')
		else:
			self.openText.set('open')

	def click_send(self):
		pass

	def setBaudrate(self):
		pass


if __name__ == '__main__':
	root = Tk()
	root.title("serial tool")

	serial_ui(root)

	root.mainloop()