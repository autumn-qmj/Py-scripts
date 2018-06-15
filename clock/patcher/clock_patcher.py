#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'clock patcher'

__author__ = 'cc'

import os
import re
import argparse
from xml_analysis import *

CLOCK_PATCHER_SUPPORT_DEVICES_KEY='support_devices'
CLOCK_PATCHER_NAME="fsl_clock.c"
CLOCK_PATCHER_FUNCTION=[]
CLOCK_PATCHER_SUPPORT_DEVICE=''
CLOCK_PATCHER_SDK_DEVICES='\\devices\\'
CLOCK_PATCHER_SDK_DEVICES_DRIVERS='\\drivers'

def add_subdir(path, sub):
	return path+'\\'+sub

def clock_section_anaysis(section):
	subsection=re.split(r'//\*function_', section)
	dict={}
	#print subsection
	for i in subsection:
		if '#' in i:
			dict[i.split('#')[0]]=i.split('#')[1]
	return dict

def clock_analysis(path):
	#print path
	with open(path) as fd:
		patch=fd.read()
	section=re.split(r'//\*function_start\*/', patch)
	return map(clock_section_anaysis, section)	

def clock_patcher_find_devices(target, path):
	path=path+CLOCK_PATCHER_SDK_DEVICES
	l=os.listdir(path)
	nl=[]
	for d in l:
		if target in d.lower():
			nl.insert(0, d)
	return nl

def clock_patcher_merge_dependency(code, func, path):
	#check dependency
	depend=func['depend'].replace('\n', '')
	if 'F:' in depend:
		if depend.replace('F:','') not in code:
			return False
	elif 'R:' in depend:
		if depend.replace('R:','') not in xml_peripheral_reg(xml_analysis(device, peripheral, path)):

# def clck_patcher_merge_update(func, newPath):
# 	with open(newPath) as fr:
# 		code=fr.read()	
# 	#get index
# 	index=code.find(func['name'].replace('\n', ''))
# 	bodyindex=code.find('\n{', index)
# 	bodyendindex=code.find('\n}', index)
# 	funccode=code[bodyindex:bodyendindex]
# 	if func['body_old'] in funccode:
# 		newfunccode=funccode.replace(func['body_old'], func['body_new'])
# 		code=code.replace(funccode, newfunccode)
# 		with open(newPath, 'w') as fw:
# 			fw.write(code)
# 		print newPath+'\n************update finish*************'

def clck_patcher_merge_new(func, newPath):
	with open(newPath) as fr:
		code=fr.read()	
	if func['body_new'] not in code:
		#get index
		index=code.find(func['depend'].replace('\n', ''))
		if func['position'].replace('\n', '')=='end':
			index=code.find('\n}', index)+1
		if func['position'].replace('\n', '')=='before':
			index=index-1
		#analysis code patch dependency
		patch=clock_patcher_merge_dependency(func['body_new'])

		code=code[:index]+patch+code[index:]
		
		with open(newPath, 'w') as fw:
			fw.write(code)
		print newPath+'\n************add new code finish*************'

def clck_patcher_merge_replace(func, newPath):
	with open(newPath) as fr:
		code=fr.read()	
	if func['depend'] in code:
		#get index
		index=code.find(func['depend'].replace('\n', ''))
		if func.has_keys('body_old'):
			if func['body_old'] in funccode:
				oldercode=clock_patcher_merge_dependency(func['body_old'])
				patch=func['body_new']
				endindex=code.find(oldercode, index)+len(oldercode)
		elif func.has_keys('body_new'):
			endindex=code.find('\n}', index)+2
			#code=code[:index]+func['body_new']+code[endindex:]
			patch=func['body_new']
		elif func.has_keys('name_new'):
			endindex=code.find('\n{', index)
			#code=code[:index]+func['name_new']+code[endindex:]
			patch=func['name_new']

		#analysis code patch dependency
		patch=clock_patcher_merge_dependency(patch)
		#merge into the codebase
		code=code[:index]+patch+code[endindex:]
		#write into file
		with open(newPath, 'w') as fw:
			fw.write(code)
		print newPath+'\n************replace code finish*************'

def clock_patcher_merge(list, path, device):
	path=path+CLOCK_PATCHER_SDK_DEVICES+device+CLOCK_PATCHER_SDK_DEVICES_DRIVERS
	if os.access(path, os.F_OK):
		for func in list:
			#if status is ignore, skipped
			if func['status'].replace('\n', '')=='ignore':
				continue
			#add location to get file content
			newPath=add_subdir(path, func['location'].replace('\n', ''))

			if func['status'].replace('\n', '')=='new':
				clck_patcher_merge_new(func, newPath)
			# elif func['status'].replace('\n', '')=='update':
			# 	clck_patcher_merge_update(func, newPath)
			elif func['status'].replace('\n', '')=='replace':
				clck_patcher_merge_replace(func, newPath)
	else:
		print path+' not exist'

def clock_patcher(list, path):
	#list0 is the support devices name
	targetDevices=list[0][CLOCK_PATCHER_SUPPORT_DEVICES_KEY].replace('\n','')
	new=list[1:]
	#get support devices
	supportDevice=clock_patcher_find_devices(targetDevices, path)
	#print new
	for device in supportDevice:
		clock_patcher_merge(new, path, device)

def clock_updater(devices, sdkpath):
	path=add_subdir(os.getcwd(), devices)
	print 'clock patch path is:'
	print path
	if os.access(path, os.F_OK):
		os.chdir(path)
		print "Prepare to analysis clock patch"
		clock_patcher(clock_analysis(add_subdir(path,CLOCK_PATCHER_NAME)), sdkpath)
	else:
		print('can not access the input path')

def clock_patcher_get_sdk_path():
	pathFile=os.getcwd()+'\\path.txt'
	with open(pathFile) as f:
			path=f.read()
	return path

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="clock patcher")

	parser.add_argument("-d", "--devices", type=str, help="device name, i.e. LPC8XX", required=True)

	args = parser.parse_args()
	devices = args.devices

	sdkpath=clock_patcher_get_sdk_path()
	print 'target sdk path is:'
	print sdkpath

	clock_updater(devices, sdkpath)

