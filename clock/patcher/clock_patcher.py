#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'generator clock code automatically'

__author__ = 'cc'

import os
import re
import argparse

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

def clck_patcher_merge_update(code, func, newPath):
	#get index
	index=code.find(func['name'].replace('\n', ''))
	bodyindex=code.find('\n{', index)
	bodyendindex=code.find('\n}', index)
	funccode=code[bodyindex:bodyendindex]
	if func['body_old'] in funccode:
		newfunccode=funccode.replace(func['body_old'], func['body_new'])
		code=code.replace(funccode, newfunccode)
		with open(newPath, 'w') as fw:
			fw.write(code)
		print newPath+'\n************update finish*************'

def clck_patcher_merge_new(code, func, newPath):
	if func['body_new'] not in code:
		#get index
		index=code.find(func['depend'].replace('\n', ''))
		if func['position'].replace('\n', '')=='end':
			index=code.find(';', index)+1
		code=code[:index]+func['body_new']+code[index:]
		with open(newPath, 'w') as fw:
			fw.write(code)
		print newPath+'\n************add new func finish*************'

def clck_patcher_merge_replace(code, func, newPath):
	if func['depend'] in code:
		#get index
		index=code.find(func['depend'].replace('\n', ''))
		endindex=code.find('\n}', index)+2
		code=code[:index]+func['body_new']+code[endindex:]
		with open(newPath, 'w') as fw:
			fw.write(code)
		print newPath+'\n************replace func finish*************'


def clock_patcher_merge(list, path):
	for func in list:
		#if status is ignore, skipped
		if func['status'].replace('\n', '')=='ignore':
			continue
		#add location to get file content
		newPath=add_subdir(path, func['location'].replace('\n', ''))
		with open(newPath) as fr:
			code=fr.read()

		#check dependency
		if func['depend'].replace('\n', '') not in code:
			continue

		if func['status'].replace('\n', '')=='new':
			clck_patcher_merge_new(code, func, newPath)
		elif func['status'].replace('\n', '')=='update':
			clck_patcher_merge_update(code, func, newPath)
		elif func['status'].replace('\n', '')=='replace':
			clck_patcher_merge_replace(code, func, newPath)


def clock_patcher(list, path):
	#list0 is the support devices name
	suppotDevices=list[0][CLOCK_PATCHER_SUPPORT_DEVICES_KEY].replace('\n','')
	new=list[1:]
	#print new
	devicesPath=[path+CLOCK_PATCHER_SDK_DEVICES+x+CLOCK_PATCHER_SDK_DEVICES_DRIVERS for x in clock_patcher_find_devices(suppotDevices, path)]
	for device in devicesPath:
		if os.access(device, os.F_OK):
			clock_patcher_merge(new, device)
		else:
			print devicesPath+' not exist'

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

