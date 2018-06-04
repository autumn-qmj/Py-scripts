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
ScriptsPath = 'C:\\Users\\nxa34233\\cc\\scripts\\python\\Py-scripts\\clock\\'
WorkPath = 'C:\\Users\\nxa34233\\cc\\SDK\\mcu-sdk-2.0\\boards\\'
c_file = '\\clock_config.c'

origin_string='''
    * 1.set the run mode to a safe configurations.
    * 2.set the PLL or FLL output target frequency for HSRUN mode.
    * 3.switch to RUN mode maximum frequency value.
    * 4.switch to HSRUN mode.
    * 5.switch to HSRUN mode maximum requency value.'''

replace_string='''
	* 1.set the run mode to a safe configurations.
    * 2.set the PLL or FLL output target frequency for HSRUN mode.
    * 3.switch RUN mode configuration.
    * 4.switch to HSRUN mode.
    * 5.switch to HSRUN mode target requency value.'''

key1=[]
replace_dict={}

def filter_device(f):
	if re.search("lpc" ,f):
		return False
	return True

#def analysis_func(func):
def add_declear(f):
	cp=f+c_file
	print cp
	try:
		fd = open(cp, 'r')
		cf=fd.read()
		fd.close()
		if origin_string in cf:
			fd2 = open(cp, 'w')
			fd2.write(cf.replace(origin_string, replace_string))
			fd2.close()
		
	except IOError,(errno, strerror):
		print(f[0]+'I/O error(%s):%s' %(errno, strerror))
	
		
def filter_dir(x):
	if os.path.isdir(x):
		return True
	return False

def update_example(l):
	sl=os.listdir(l)
	sl=[l+ "\\" +x for x in sl]
	l=filter(filter_dir, sl)
	print(l)


print 'update clock'
filePath = WorkPath
if os.access(filePath, os.F_OK):
	os.chdir(filePath)
else:
	print('can not access the input path')
print(os.getcwd())
l=os.listdir(filePath)
print l
#specifiy the board
l = filter(filter_device, l)

l = [filePath + x for x in l]
print l
#specifiy the driver dir
l=filter(filter_dir, l)
print (l)
#add file name

map(add_declear, l)
