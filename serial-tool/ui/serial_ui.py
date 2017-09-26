#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'serial tool UI'


__author__ = 'cc'

from Tkinter import *
from ttk import *
import ScrolledText as st
import serial


ConfigurationLabel = ['baudrate', 'bytesize', 'parity', 'stopbits', 'xonxoff', 'rts', 'dtr']
BaudrateList = [256000, 128000, 115200, 57600, 56000, 38400, 19200, 14400, 9600, 4800, 2400, 1200, 600, 300]
BytesizeList = {'5':serial.FIVEBITS, '6':serial.SIXBITS, '7':serial.SEVENBITS, '8':serial.EIGHTBITS}
ParityList = {'None' : serial.PARITY_NONE, 'Odd' : serial.PARITY_ODD, 'Even' : serial.PARITY_EVEN, 'Mark': serial.PARITY_MARK, 'Space': serial.PARITY_SPACE}
StopbitsList = {'1' : serial.STOPBITS_ONE, '1.5' : serial.STOPBITS_ONE_POINT_FIVE, '2' : serial.STOPBITS_TWO}
FlowCtrlList= {'Disable' : False, 'Software' : False}
DtrrtsList = {'Disable' : False, 'Enable' : True}

class Serial_ui(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.pack(fill=BOTH, expand = True)

		self.confFrame = LabelFrame(self)
		self.confFrame.grid(row = 0, column = 0, sticky = 'wesn', columnspan = 2)
		self.recvframe = LabelFrame(self)
		self.recvframe.grid(row = 0, column = 1, sticky = 'wesn', columnspan = 4, rowspan = 2)
		self.confBotFrame = LabelFrame(self)
		self.confBotFrame.grid(row = 1, column = 0, sticky = 'wesn')
		self.statusframe = LabelFrame(self)
		self.statusframe.grid(row = 2, column = 0, sticky = 'wesn', columnspan = 2)
		self.sendframe = LabelFrame(self)
		self.sendframe.grid(row = 2, column = 2, sticky = 'wesn', columnspan = 3)

		self.create_configuration_top_frame()
		self.create_configuration_bot_frame()		
		self.create_send_frame()
		self.create_recv_frame()
		self.create_status_frame()
		
	def create_send_frame(self):
		buttonReset = Button(self.sendframe, text='reset', command = self.click_reset).grid(column=0, row=0)
		#send button
		self.sendText = StringVar()
		Entry(self.sendframe, width = 40, textvariable = self.sendText).grid(column=2, row=0)
		Button(self.sendframe, text='browse', command = self.click_browse).grid(column=3, row=0)
		Button(self.sendframe, text='send', command = self.click_send).grid(column=4, row=0)
		
	def create_recv_frame(self):
		self.recvText = st.ScrolledText(self.recvframe, width = 100, height = 35)
		self.recvText.grid(column=0, row=0, sticky = 'wesn')
	# def create_configuration_frame(self):
	# 	#self.confTopFrame = LabelFrame(self.confFrame)
	# 	#self.confTopFrame.grid(row = 0, column = 0, padx = 0, pady = 0, sticky = 'n')

	def create_configuration_top_frame(self):
		self.comList = StringVar()
		#select mode:browse, extended
		#func:curselection(), return the current select item
		#selection_set(index), set item to select
		#see(index), check the item is avaliable or not
		#listbox.bind('<<ListboxSelect>>', func)
		self.listbox = Listbox(self.confFrame, height = 22, width = 27, listvariable = self.comList, selectmode = 'browse', bg = 'WhiteSmoke')
		self.listbox.grid(row = 0, column = 0, sticky = 'wesn') 
		self.listbox.bind('<<ListboxSelect>>', self.selectComPortList)

	def create_configuration_bot_frame(self):
		for index, l in enumerate(ConfigurationLabel):
			Label(self.confBotFrame, text=l).grid(column=0, row=index+1, sticky = 'w')

		#refresh button
		buttonRefresh = Button(self.confBotFrame, text='refresh', command = self.click_refresh).grid(column=0, row=0)

		#open button
		self.openText = StringVar()
		self.openText.set('open')
		buttonOpen = Button(self.confBotFrame, textvariable=self.openText, command = self.click_open).grid(column=1, row=0)

		#baudrate combobox
		self.baudrate = Combobox(self.confBotFrame, values = BaudrateList, state = 'readonly', width = 10)
		self.baudrate.grid(column=1, row=1, pady = 5)
		self.baudrate.current(2)
		#bytesize combobox
		self.bytesize = Combobox(self.confBotFrame, values = BytesizeList.keys(), state = 'readonly', width = 10)
		self.bytesize.grid(column=1, row=2)
		self.bytesize.current(0)
		#parity combobox
		self.parity = Combobox(self.confBotFrame, values = ParityList.keys(), state = 'readonly', width = 10)
		self.parity.grid(column=1, row=3)
		self.parity.current(1)
		#stopbits combobox
		self.stopbits = Combobox(self.confBotFrame, values = StopbitsList.keys(), state = 'readonly', width = 10)
		self.stopbits.grid(column=1, row=4)
		self.stopbits.current(0)
		#flow control combobox
		self.flowctrl = Combobox(self.confBotFrame, values = FlowCtrlList.keys(), state = 'readonly', width = 10)
		self.flowctrl.grid(column=1, row=5)
		self.flowctrl.current(0)
		#rts checkbutton
		self.rts = Combobox(self.confBotFrame, values = DtrrtsList.keys(), state = 'readonly', width = 10)
		self.rts.grid(column=1, row=6)
		self.rts.current(0)
		#dtr checkbutton
		self.dtr = Combobox(self.confBotFrame, values = DtrrtsList.keys(), state = 'readonly', width = 10)
		self.dtr.grid(column=1, row=7)
		self.dtr.current(0)
		
	def create_status_frame(self):
		self.statusText = StringVar()
		self.statusBar = Label(self.statusframe, width = 60, textvariable = self.statusText, background = 'WhiteSmoke').grid(column=0, row=0)

	def click_open(self):
		self.recvText.insert(END, 'TEST\n')
		self.recvText.see(END)

	def click_send(self):
		pass

	def click_browse(self):
		pass

	def click_refresh(self):
		pass

	def selectComPortList(self, event):
		pass

	def click_reset(self):
		self.recvText.delete(0.0, END)
		self.sendText.set('')

if __name__ == '__main__':
	root = Tk()
	root.title("serial tool")

	s=Serial_ui(root)
	s.listbox.insert(END, 'COM1')
	s.listbox.insert(END, 'COM2')
	root.mainloop()