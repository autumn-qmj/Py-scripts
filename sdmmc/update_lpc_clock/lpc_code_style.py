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
BoardFilterString='LPC'
ExampleFilterString = 'fsl_clock.c'
function_name = 'uint32_t CLOCK_GetFreq(clock_name_t clockName)'
function_case = 'case '
function_end = 'default'
function_break = 'break'
function_div = 'DIV'

key1=[]
replace_dict={}

# template ='
#     uint32_t freq = 0U;

#     switch(sel)
#     {
#         case 0U:
#           freq = CLOCK_GetCoreSysClkFreq();
#           break;
#         case 1U:
#           freq = CLOCK_GetPllOutFreq();
#           break;
#         case 2U:
#           freq = CLOCK_GetUsbPllOutFreq();
#           break;
#         case 3U:
#           freq = CLOCK_GetFroHfFreq();
#           break;
#         case 4U:
#           freq = CLOCK_GetAudioPllOutFreq();
#           break;
#         case 7U:
#           freq = 0U;
#           break;
#         default:
#           break;
#     }

#     return freq / ((SYSCON->SDIOCLKDIV&0xffU)+1U);
# }'

def filter_device(f):
	if re.search(BoardFilterString ,f):
		return True
	return False

#def analysis_func(func):

def update_code(f, key, index):
	t=[]
	t1=[]
	pre=[]
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
					found=False
					break

		f2.close()

		t=[x.replace('return ', 'return (') for x in t]
		t=[x.replace(';', ');') for x in t]

		value= replace_dict[key1[index]]
		
		t=[x.replace(');', ') / ' + value + ';') for x in t]
		t1 = ''.join(t)

		f2 = open(f, 'r')
		for line in f2.readlines():

			value = ''.join(key1[index] + ' / ')
			#print value
			if value in line:
				pre.append('						freq = ' + key1[index] + ';\n')
				continue
			if key[index] in line:
				pre.append(t1)
				found=True

			if found == False:
				pre.append(line)
			elif '}' in line:
				found=False
		f2.close()

		print t1


		f2 = open(f, 'w+')
		pre = f2.writelines(pre)
		f2.close()


	except IOError,(errno, strerror):
		print(f[0]+'I/O error(%s):%s' %(errno, strerror))

def get_func(f):
	found = False;
	new = []
	function = []

	try:
		f1=open(f, 'r')
		
		for line in f1.readlines():
			
			if found:
				if '}' in line:
					found = False
				function.append(line)
			else:
				new.append(line)

			if 'uint32_t CLOCK_Get' in line:
				if 'uint32_t CLOCK_GetFreq' in line:
					continue
				found = True

		print function

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

l = [filePath + x + device_driver for x in l]
#specifiy the driver dir
l=filter(filter_dir, l)
#add file name
l = [x + ExampleFilterString for x in l]
print l
print len(l)

get_func(l[0])