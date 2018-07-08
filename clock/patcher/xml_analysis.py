#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'analysis device xml file'

__author__ = 'cc'

import os
import re
import argparse


# div_str='Divider'
# mux_str='Selector'
# gate_str='_clk_enable'
# field_str='<field>'

# def get_div(reg, field):
# 	d={}
# 	md=[]
# 	d['reg']=reg[0].replace('name', '').replace('<>', '')
# 	d['name']=field[0].replace('name', '').replace('<>', '')
# 	d['offset']=field[2].replace('bitOffset', '').replace('<>', '')
# 	d['width']=field[3].replace('bitWidth', '').replace('<>', '')
# 	new=field[5:-1]
# 	md=[(new[x*3+1].replace('<description>divide by ', '')+'-'+new[x*3+2].replace('<value>', '')) for x in range(len(new)/3)]
# 	d['value']=md
# 	CLOCK_DIV.insert(-1, d)

# def get_mux(reg, field):
# 	m={}
# 	m['reg']=reg[0].replace('name', '').replace('<>', '')
# 	m['name']=field[0].replace('name', '').replace('<>', '')
# 	m['offset']=field[2].replace('bitOffset', '').replace('<>', '')
# 	m['width']=field[3].replace('bitWidth', '').replace('<>', '')
# 	nm=field[5:-1]
# 	mg=[(nm[x*3+1].replace('<description>derive clock from ', '')+'-'+nm[x*3+2].replace('<value>', '')) for x in range(len(nm)/3)]
# 	m['value']=mg
# 	CLOCK_MUX.insert(-1, m)

# def get_gate(reg, field):
# 	g={}
# 	g['reg']=reg[0].replace('name', '').replace('<>', '')
# 	g['name']=field[1].replace('description', '').replace('<>', '')
# 	g['offset']=field[2].replace('bitOffset', '').replace('<>', '')
# 	g['width']=field[3].replace('bitWidth', '').replace('<>', '')
# 	CLOCK_GATE.insert(-1, g)

def xml_find_peripherals(f):
	p=re.findall(r'<peripheral>\n\s{3,}<name>\w{2,}', f, re.S)
	for o in p:
		print re.search(r'<name>\w+', o).group()

def xml_convert_dict(s):
	if s:
		l1=re.findall(r'<\w*>',s)
		#print l1
		l2=re.findall(r'>.*<', s)
		#print l2
		l1=[x.replace('<','').replace('>','') for x in l1]
		l2=[x.replace('>','').replace('<','') for x in l2]
		d= dict(zip(l1,l2))
		return d
	#s=re.sub(r'</\w*>','',s).replace('<','')

def xml_reg_field(field):
	enumIndex=field.find('<enumeratedValues>')
	f=xml_convert_dict(field[:enumIndex])
	enum=re.split(r'<enumeratedValue>', field[enumIndex:])[1:-2]
	fields=[xml_convert_dict(x) for x in enum]
	f['enumeratedValue']=fields
	print f
	return f

def xml_reg_analysis(reg):
	fieldIndex=reg.find('<field>')
	register=xml_convert_dict(reg[:fieldIndex])
	#fields=re.findall(r'<field>(.|\n)*<\field>', reg[fieldIndex:])
	fields=re.split(r'<field>', reg[fieldIndex:])[1:]
	fields=[xml_reg_field(x) for x in fields]
	register['fields']=fields
	return register

def xml_peripheral_reg(f, peripheral):
    ps=f.find('<name>'+peripheral+'</name>')
    ps=f.find('<register>', ps)
    pe=f.find('</peripheral>', ps, len(f))
    #print f[ps:pe].replace(' ', '')
    regs=re.split(r'<register>', f[ps:pe])[1:]
    #print regs
    regs=[xml_reg_analysis(x) for x in regs]
    return regs

def xml_analysis(device, peripheral, xmlPath):
	with open(xmlPath+'/'+device+'.xml') as fd:
		xml=fd.read()
	#xml_find_peripherals(xml)
	return xml_peripheral_reg(xml, peripheral)

def xml_get_peripheral_regs(regs):
	return [x['name'] for x in regs]

def xml_get_periperal_regs_bits(regs,reg):
	reglist=xml_get_peripheral_regs(regs)
	if reg in reglist:
		#print regs[reglist.index(reg)]
		return [x['name'] for x in regs[reglist.index(reg)]['fields']]
	else:
		print 'not support register'

# def xml_get_peripheral_regs_type_div(regs):
# 	l=[]
# 	for x in regs:
# 		for y in x['fields']:
# 			if 'divider' in y['description']:
# 				print y['description']
# 				l.append(x['name'])
# 	return l

temppath='C:\\Users\\cc\\Desktop\\scripts\\Py-scripts\\clock\\patcher\\sdk\\devices\\LPC845'
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="generator clock automatically")

	parser.add_argument("-c", "--cpu", type=str, help="CPU name, i.e. MK64F12", required=True)
	parser.add_argument("-p", "--peripheral", type=str, help="Peripheral name, i.e. SYSCON", required=True)

	args = parser.parse_args()
	cpu = args.cpu
	p = args.peripheral

	regs=xml_analysis(cpu, p, temppath)

	print xml_get_peripheral_regs(regs)
	print xml_get_periperal_regs_bits(regs, 'FROOSCCTRL')
	#print xml_get_peripheral_regs_type_div(regs)