import os

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

def append_string(x):
	l=os.listdir(x)
	l= [x+'\\'+i+'\\drivers\\fsl_clock.c' for i in l if os.path.isdir(i)]
	print(l)
	return l

def find_replace_string(l, s, r):
	needUpdate = False
	for d in l:
		data=''
		try:
			f=open(d, 'r+')
			for line in f:
				if s in line:
					print('match file' + d)
					#line=line.replace(s, r)
					#needUpdate = True
				data += line
			f.close()
			# if needUpdate:
			# 	f=open(d, 'w+')
			# 	f.writelines(data)
			# 	needUpdate = False
			# 	f.close()
		except IOError,(errno, strerror):
			print(d+'I/O error(%s):%s' %(errno, strerror)) 
		

print('Input path:')
s=raw_input()
if os.access(s, os.F_OK):
	os.chdir(s)
else:
	print('can not access the input path')

print(os.getcwd())
l=append_string(s)
print('Input compare pattern:')
s=raw_input()
r = None
#print('Input replace pattern:')
#r=raw_input()
find_replace_string(l, s, r)
