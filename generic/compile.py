#!/usr/bin/python3.6

import os, sys, subprocess, configparser
from configure import Configuration
config = configparser.ConfigParser()

class Compile(object):
	''' Stores configuration variables and functions for Compile. '''
	version = '1.1.1'
		
	out = subprocess.getstatusoutput
	history = []

	colors = {
		'W' : '\033[1;97m', # white (normal)
		'R' : '\033[1;91m', # red
		'G' : '\033[1;92m', # green
		'O' : '\033[1;93m', # orange
		'B' : '\033[1;94m', # blue
		'P' : '\033[1;95m', # purple
		'C' : '\033[1;96m', # cyan
		'GR': '\033[37m',   # gray
		'D' : '\033[2m',    # dims current color. {W} resets.

		'Wx' : '\033[0m',  # white (normal)
		'Rx' : '\033[31m', # red
		'Gx' : '\033[32m', # green
		'Ox' : '\033[33m', # orange
		'Bx' : '\033[34m', # blue
		'Px' : '\033[35m', # purple
		'Cx' : '\033[36m', # cyan
		'GRx': '\033[37m', # gray

	}

	replacements = {
		'{+}': ' {W}{D}[{W}{G}+{W}{D}]{W}',
		'{!}': ' {O}[{R}!{O}]{W}',
		'{?}': ' {W}[{C}?{W}]'
	}

	@staticmethod
	def s(text):
		output = text
		for (key,value) in Compile.replacements.items():
			output = output.replace(key, value)
		for (key,value) in Compile.colors.items():
			output = output.replace("{%s}" % key, value)
		return output

	@staticmethod
	def exec_(exec_c, name):
		os.system('gcc -Wall -D_GNU_SOURCE '+exec_c+' -o '+name+' && ./'+name)
		os.system('rm ./'+name)

	@staticmethod
	def exists_(exec_c):
		if exec_c[0] == 'c':
			if exec_c[1] in Compile.get_ls()[1]:
				name = ''
				for y in exec_c[1]:
					if y == '.': break
					else: name = name+y
				Compile.exec_(exec_c[1], name)

	@staticmethod
	def get_ls():
		listDIR = Compile.out('ls')[1].split()
		listDIRstr = ''
		for y in listDIR:
			listDIRstr = listDIRstr + ' ' + y

		return listDIR, listDIRstr

	@classmethod
	def quest(cls):
		user = 'user'
		while True:
			exec_c = input(Compile.s("{P}[ {Rx}{}{P} ]{G}#{Ox} ").format(user))
			print(Compile.s("{Gx}"), end='')
			Compile.history.append(exec_c.split())
			if exec_c == 'exit': exit()
			elif exec_c == 'ls': print(Compile.get_ls()[1])
			elif exec_c == 'quit': exit()
			elif exec_c == 'cls': os.system('clear')
			elif exec_c == 'y': Compile.exists_(Compile.history[0])
			else:
				Compile.exists_(exec_c.split())

if __name__ == '__main__':
	Compile().quest()