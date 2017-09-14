#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Check and update sdmmc example requirement in yml file '


__author__ = 'cc'

import os
import re

#flush, flush the internal buffer, like the stdio's fflush, use flush followed by os.sync() to ensure this behaviour.
#fileno(), return the integer "file descriptor".
#isatty(), return true if the file is connected to a tty device else false.
#next(), return the next input line
#read([size]), read at most size bytes from the file.If the size argument is negative or omitted, read all data until EOF is reach.
#the bytes are returned as a string object.
#readline([size]), read one enire line from the file or incomplete line.The returned string contains null characters('\0')if they occured in the input.
#readlines([size]),
#seek(offset[, whence]), f.seek(2, os.SEEK_CUR)
#tell return the file current position
#truncate([size]) truncate the file's size.
#write(str) write a string to the file.There is no return value.Due to buffering, the string may not
#actually show up until the flush() or close()
#writelines(sequence) write a sequence of strings to the file.

# f = open("test.txt", 'w')
# # for line in f:
# # 	print line.strip()
# s = ["cc", 'dd',];
# f.writelines(s)

# f.flush()

# f.close()
ScriptsPath = 'C:\\CC\work\\scripts\\check sdmmc example in yml and update\\'
WorkPath = 'C:\\CC\\work\\'
FilePath = '\\bin\\generator\\records\\msdk\\projects\\sdk_example\\'
BoardFilterString='.yml'
ExampleFilterString = 'sdcard'

def filter_board(f):
	if re.search(BoardFilterString ,f):
		return True
	return False

def filter_example(l):
	try:
		f=open(filePath+l, 'r+')
		for line in f:
			if ExampleFilterString in line:
				f.close()
				return True
		f.close()
	except IOError,(errno, strerror):
		print(l+'I/O error(%s):%s' %(errno, strerror)) 
	return False

def update_example(l):
	f=open(l, 'r')
	f1=open(ScriptsPath + 'mmc.yml', 'r')
	f2=f.read()+f1.read()
	f.close()
	f1.close()
	f=open(l, 'w+')
	f.writelines(f2)
	f.close()
	return False

print('Input SDK path:')
sdkPath = raw_input()
filePath = WorkPath + sdkPath + FilePath
if os.access(filePath, os.F_OK):
	os.chdir(filePath)
else:
	print('can not access the input path')
print(os.getcwd())
l=os.listdir(filePath)
#specifiy the board
l = filter(filter_board, l)
print(l)
#specifiy the example
l=filter(filter_example, l)
print('Total boards: %d\n'%len(l))
print(l)
#l=map(update_example, l)
