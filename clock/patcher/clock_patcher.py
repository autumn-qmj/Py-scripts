#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'clock patcher'

__author__ = 'cc'

import os
import re
import argparse
from xml_analysis import *

CLOCK_PATCHER_SUPPORT_DEVICES_KEY='support_devices'
CLOCK_PATCHER_FUNCTION=[]
CLOCK_PATCHER_SUPPORT_DEVICE=''
CLOCK_PATCHER_SDK_DEVICES='\\devices\\'
CLOCK_PATCHER_SDK_DEVICES_DRIVERS='drivers'

def add_subdir(path, *dir):
	for x in dir:
		path=path+'\\'+x
	return path

def clock_section_anaysis(section):
	subsection=re.split(r'//\*function_', section)
	dict={}
	#print subsection
	for i in subsection:
		if '#' in i:
			dict[i.split('#')[0]]=i.split('#')[1]
	return dict

def clock_analysis(path):
	files=os.listdir(path)
	dict={}
	for f in files:
		with open(add_subdir(path, f)) as fd:
			patch=fd.read()
		section=re.split(r'//\*function_start\*/', patch)
		dict[f]=map(clock_section_anaysis, section[1:])
	return dict

def clock_patcher_find_devices(target, path):
	path=path+CLOCK_PATCHER_SDK_DEVICES
	l=os.listdir(path)
	nl=[]
	for d in l:
		if target in d.lower():
			nl.insert(0, d)
	return nl

def clock_patcher_merge_dependency(patch, path, device):
	#check dependency
	section=re.split(r'\$\$\n', patch)
	xml=xml_analysis(device, 'SYSCON', path)
	regs=xml_get_peripheral_regs(xml)
	newPatch=section[0]
	for x in section[1:]:
		subsection=re.split(r'@', x)
		if 'R' in subsection:
			dr=subsection[subsection.index('R')+1]
			if dr in regs:
				if 'RB' in subsection:
					regbits=xml_get_periperal_regs_bits(xml, dr)
					drb=subsection[subsection.index('RB')+1]
					print drb
					print regbits
					if drb in regbits:
						newPatch=newPatch + str(subsection[subsection.index(drb)+1])
				else:
					newPatch=newPatch + str(subsection[subsection.index(dr)+1])
			else:
				print 'tets'
		else:
			newPatch=newPatch + str(subsection[0])
	return newPatch
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

def clck_patcher_merge_new(func, path, device):
	newPath=add_subdir(path, CLOCK_PATCHER_SDK_DEVICES_DRIVERS, func['location'].replace('\n', ''))
	with open(newPath) as fr:
		code=fr.read()	
	if func['depend'] in code:
		#get index
		index=code.find(func['depend'].replace('\n', ''))
		#if target position is header file, then put it after dependency.
		if func['location'].replace('\n', '')=='fsl_clock.h':
			index +=len(func['depend'])
		#if target position is in source file, then put it before dependency.
		else:
			index=index-1
		#analysis code patch dependency
		patch=clock_patcher_merge_dependency(func['body_new'], path, device)

		code=code[:index]+patch+code[index:]
		
		with open(newPath, 'w') as fw:
			fw.write(code)
		print newPath+'\n************add new code finish*************'

def clck_patcher_merge_replace(func, path, device):
	newPath=add_subdir(path, CLOCK_PATCHER_SDK_DEVICES_DRIVERS, func['location'].replace('\n', ''))
	with open(newPath) as fr:
		code=fr.read()	
	if func['depend'] in code:
		#get index
		index=code.find(func['depend'].replace('\n', ''))
		if func.has_key('body_old'):
			oldercode=clock_patcher_merge_dependency(func['body_old'], path, device)
			if oldercode in code[index:]:
				patch=func['body_new']
				newindex=code.find(oldercode)
				#analysis code patch dependency
				patch=clock_patcher_merge_dependency(patch, path, device)
				#merge into the codebase
				code=code[:newindex]+patch+code[newindex+len(oldercode):]
			else:
				print oldercode + 'not found'
		if func.has_key('name_new'):
			endindex=code.find('\n{', index)
			#code=code[:index]+func['name_new']+code[endindex:]
			patch=func['name_new']
			#analysis code patch dependency
			patch=clock_patcher_merge_dependency(patch, path, device)
			#merge into the codebase
			code=code[:index]+patch+code[endindex:]
		#write into file
		with open(newPath, 'w') as fw:
			fw.write(code)
		print '\n************replace code finish*************'

def clock_patcher_merge(list, path, device):
	path=path+CLOCK_PATCHER_SDK_DEVICES+device
	if os.access(path, os.F_OK):
		for func in list:
			#if status is ignore, skipped
			if func['status'].replace('\n', '')=='ignore':
				continue
			#add location to get file content
			# newPath=add_subdir(path, func['location'].replace('\n', ''))

			if func['status'].replace('\n', '')=='new':
				clck_patcher_merge_new(func, path, device)
			# elif func['status'].replace('\n', '')=='update':
			# 	clck_patcher_merge_update(func, newPath)
			elif func['status'].replace('\n', '')=='replace':
				clck_patcher_merge_replace(func, path, device)
	else:
		print path+' not exist'

def clock_patcher(dict, path, devices):
	#get support devices
	supportDevice=clock_patcher_find_devices(devices, path)
	for device in supportDevice:
		print 'updating device: ' + device
		for list in dict.values():
			clock_patcher_merge(list, path, device)

def clock_updater(devices, sdkpath):
	path=add_subdir(os.getcwd(), devices)
	print 'clock patch path is:'
	print path
	if os.access(path, os.F_OK):
		os.chdir(path)
		print "Prepare to analysis clock patch"
		clock_patcher(clock_analysis(path), sdkpath, devices)
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

