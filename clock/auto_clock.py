#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'generator clock code automatically'

__author__ = 'cc'

import os
import re
import argparse


div_str='Divider'
mux_str='Selector'
gate_str='_clk_enable'
field_str='<field>'

CLOCK_DIV=[]
CLOCK_MUX=[]
CLOCK_GATE=[]


def get_div(reg, field):
	d={}
	md=[]
	d['reg']=reg[0].replace('name', '').replace('<>', '')
	d['name']=field[0].replace('name', '').replace('<>', '')
	d['offset']=field[2].replace('bitOffset', '').replace('<>', '')
	d['width']=field[3].replace('bitWidth', '').replace('<>', '')
	new=field[5:-1]
	md=[(new[x*3+1].replace('<description>divide by ', '')+'-'+new[x*3+2].replace('<value>', '')) for x in range(len(new)/3)]
	d['value']=md
	CLOCK_DIV.insert(-1, d)

def get_mux(reg, field):
	m={}
	m['reg']=reg[0].replace('name', '').replace('<>', '')
	m['name']=field[0].replace('name', '').replace('<>', '')
	m['offset']=field[2].replace('bitOffset', '').replace('<>', '')
	m['width']=field[3].replace('bitWidth', '').replace('<>', '')
	nm=field[5:-1]
	mg=[(nm[x*3+1].replace('<description>derive clock from ', '')+'-'+nm[x*3+2].replace('<value>', '')) for x in range(len(nm)/3)]
	m['value']=mg
	CLOCK_MUX.insert(-1, m)

def get_gate(reg, field):
	g={}
	g['reg']=reg[0].replace('name', '').replace('<>', '')
	g['name']=field[1].replace('description', '').replace('<>', '')
	g['offset']=field[2].replace('bitOffset', '').replace('<>', '')
	g['width']=field[3].replace('bitWidth', '').replace('<>', '')
	CLOCK_GATE.insert(-1, g)

def analysis_reg_field(reg, field):
	#print reg
	#print field

	for bit in field:
		if div_str in bit[1]:
			get_div(reg, bit)
		elif mux_str in bit[1]:
			get_mux(reg, bit)
		elif gate_str in bit[1]:
			get_gate(reg, bit)
		else:
			pass

def analysis_reg(reg):
    lr=[]
    pre='null'
    #print reg
    for n in reg:
        if 'name' in n and pre not in n:
            lr.append(reg.index(n))
            pre=n
    l2=[reg[lr[i]:lr[i+1]] for i in range(len(lr)) if lr[i] != lr[-1]]
    l2.append(reg[lr[-1]: -1])
    #print l2
    analysis_reg_field(l2[0], l2[1:])

def find_peripherals(f):
	p=re.findall(r'<peripheral>\n\s{3,}<name>\w{2,}', f, re.S)
	for o in p:
		print re.search(r'<name>\w+', o).group()

def find_peripheral_reg(f, name):
    ln=[]
    ps=f.find('<name>'+name+'</name>')
    ps=f.find('<registers>', ps)
    pe=f.find('</peripheral>', ps, len(f))
    #print f[ps:pe].replace(' ', '')

    l=[s.replace('</', '') for s in re.findall(r'<.*</', f[ps:pe], re.M)]
    for s in range(len(l)):
        if 'Register' in l[s]:
            ln.append(s - 1)
    l1=[l[ln[i]:ln[i+1]] for i in range(len(ln)) if ln[i] != ln[-1]]
    l1.append(l[ln[-1]: -1])
    #print l1
    for r in l1:
        analysis_reg(r)

def analysis_device_xml(device):
	f = '../../devices/' + device + '/' + device + '.xml'
	with open(f) as fd:
		xml=fd.read()
	find_peripherals(xml)
	find_peripheral_reg(xml, 'CCM')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="generator clock automatically")

	parser.add_argument("-c", "--cpu", type=str, help="CPU name, i.e. MK64F12", required=True)

	args = parser.parse_args()
	cpu = args.cpu

	analysis_device_xml(cpu)

	print CLOCK_GATE
	print CLOCK_DIV
	print CLOCK_MUX