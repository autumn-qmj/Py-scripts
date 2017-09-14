#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Check and update sdmmc example readme file '


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
scriptsPath = 'C:\\CC\work\\scripts\\sdmmc driver example log update\\'
workPath = 'C:\\CC\\work\\'
examplePath = '\\driver_examples\\'
boardFilterString='src'
gitFliterString='.git'
exampleFilterString='mmccard'
contentFilterString='SDCARD'

pollingExample = exampleFilterString + '\\polling\\board.readme'
interruptExample = exampleFilterString + '\\interrupt\\board.readme'
freertosExample = exampleFilterString + '\\freertos\\board.readme'
fatfsExample = exampleFilterString + '_fatfs' + '\\board.readme'


def filter_board(f):
	if re.search(boardFilterString ,f):
		return False
	elif re.search(gitFliterString ,f):
		return False
	return True

def filter_example(l):
	if os.path.exists(l) == False:
		return False
	s=os.listdir(l)
	if exampleFilterString in s:
		return True
	return False

def update_readme(l):
	readme = {pollingExample : exampleFilterString+'_polling_readme.txt', interruptExample : exampleFilterString+'_interrupt_readme.txt', freertosExample : exampleFilterString+'_freertos_readme.txt', fatfsExample : exampleFilterString+'_fatfs_readme.txt'}
	for f in readme.items():
		try:
			f1=open(l+f[0], 'r')
			f2=open(scriptsPath + f[1], 'r')
			tf=f2.read()
			of=f1.read()

			if contentFilterString in of:
				of=of.replace(contentFilterString, tf)
				f2.close()
				f1.close()

				f1=open(l+f[0], 'w+')
				f1.writelines(of)
				f1.close()
		except IOError,(errno, strerror):
			print(f[0]+'I/O error(%s):%s' %(errno, strerror)) 

print('Input SDK path:')
sdkPath = raw_input()
tempPath = workPath + sdkPath + '\\boards\\'
if os.access(tempPath, os.F_OK):
	os.chdir(tempPath)
else:
	print('can not access the input path')
print(os.getcwd())
l=os.listdir(tempPath)

#specifiy the board
l = filter(filter_board, l)
print(l)

#specifiy the example
l=[tempPath+x+examplePath for x in l]
l=filter(filter_example, l)
print(l)

l=map(update_readme, l)
