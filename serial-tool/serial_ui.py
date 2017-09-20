#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'serial tool UI'


__author__ = 'cc'

from Tkinter import *


class serial_ui(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.pack(fill=BOTH, expand = True)

		self.openText = StringVar()
		self.sendText = StringVar()
		self.openText.set('open')
		buttonOpen = Button(self, text=self.openText.get(), command = self.click_open).grid(column=0, row=0)

		text = StringVar()
		entry = Entry(self, width = 20, textvariable = self.sendText).grid(column=0, row=1)
		buttonSend = Button(self, text='send', command = self.click_send).grid(column=4, row=1)


	def click_open(self):
		self.openText.set('close')

	def click_send(self):
		pass


if __name__ == '__main__':
	root = Tk()
	root.title("serial tool")

	serial_ui(root)

	root.mainloop()