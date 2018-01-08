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

device = '\\devices\\'
device_driver = '\\drivers\\'
BoardFilterString='LPC5'
ExampleFilterString = 'fsl_clock.c'
function_name = 'uint32_t CLOCK_GetFreq(clock_name_t clockName)'
function_case = 'case '
function_end = 'default'
function_break = 'break'
function_div = 'DIV'

key1=[]
replace_dict={}

def filter_device(f):
	if re.search(BoardFilterString ,f):
		return True
	return False

#def analysis_func(func):

def update_code(f, key, index):
	t=[]
	t1=''
	t2=''
	found=False
	value=''
	try:
		f2 = open(f, 'r')
		for line in f2.readlines():
			if key[index] in line:
				found=True
			if found:
				t.append(line)
				if '}' in line:
					break

		f2.close()

		t1 = ''.join(t)

		t=[x.replace('return ', 'return (') for x in t]
		t=[x.replace(';', ');') for x in t]

		value= replace_dict[key1[index]]
		t=[x.replace(');', ') / ' + value + ';') for x in t]
		t2 = ''.join(t)

		f2 = open(f, 'r')
		c=f2.read()
		f2.close()

		



	except IOError,(errno, strerror):
		print(f[0]+'I/O error(%s):%s' %(errno, strerror))

def get_func(f):
	found=False
	readindex = False
	index=[]
	func=[]
	key=[]
	j=0
	try:
		f1=open(f, 'r')
		
		for line in f1.readlines():
			if readindex:
				index.append(line)
				readindex=False

			if function_name in line:
				found = True

			if found == True:
				if function_case in line:
					func.append(line)
					readindex = True

				if function_end in line:
					break
		
		func = [x.replace(function_case, '') for x in func]
		func = [x.replace(':\n', '') for x in func]
		func = [x.replace('kCLOCK_', '') for x in func]
		func = [x.replace('  ', '') for x in func]
		index = [x.replace('freq = ', '') for x in index]
		index = [x.replace('  ', '') for x in index]
		index = [x.replace(' ', '') for x in index]
		index = [x.replace(';\n', '') for x in index]
		for i in func:
			pos = index[j].split('/')
			if i in pos[0]:
				if function_div in index[j]:
					replace_dict[pos[0]] = pos[1]
					key.append(pos[0])
					key1.append(pos[0])
			j = j+1

		f1.close()

		print func
		print index
		print replace_dict
		key=['uint32_t ' + x.replace('()', '') for x in key]

		update_code(f, key, 0)

	except IOError,(errno, strerror):
		print(f[0]+'I/O error(%s):%s' %(errno, strerror)) 

# def update_example(l):
# 	f=open(l, 'r')
# 	f1=open(ScriptsPath + 'mmc.yml', 'r')
# 	f2=f.read()+f1.read()
# 	f.close()
# 	f1.close()
# 	f=open(l, 'w+')
# 	f.writelines(f2)
# 	f.close()
# 	return False

def filter_dir(x):
	if os.path.isdir(x):
		return True
	return False

def update_example(l):
	sl=os.listdir(l)
	sl=[l+ "\\" +x for x in sl]
	l=filter(filter_dir, sl)
	print(l)

print('Input SDK path:')
sdkPath = raw_input()
filePath = WorkPath + sdkPath + device
if os.access(filePath, os.F_OK):
	os.chdir(filePath)
else:
	print('can not access the input path')
print(os.getcwd())
l=os.listdir(filePath)
#specifiy the board
l = filter(filter_device, l)
l.insert(1, 'LPC6324')
print(l)
l = [filePath + x + device_driver for x in l]
print(l)

#specifiy the driver dir
l=filter(filter_dir, l)
print (l)
#add file name
l = [x + ExampleFilterString for x in l]

get_func(l[2])

#map(get_func, l)
