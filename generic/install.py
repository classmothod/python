import subprocess
import os

def Folder(locale):
	if locale[0] != '/': locale = '/'+locale 
	y = subprocess.getstatusoutput('ls locale')
	if y[1] == str:
		return False
	else:
		return True

def File(locale='/etc/default/grub', txt='GRUB_THEME='):
	Arq = open(locale, 'r')
	Texto = Arq.readlines()
	for l in Texto:
		y = l.rfind(txt)
		if y != -1:
			return True
		else:
			return False


if Folder('/boot/grub') == True:
	print('\033[0;92m', '==>',"\033[1;97m",' Copying files...\n','\033[0m', sep='')
	subprocess.run(['cp','-rf', 'blur-grub2-fullhd /boot/grub/themes'])
else:
	print("\033[1;97m",'Copying files...\n','\033[0m')
	subprocess.run(['cp','-rf', 'blur-grub2-fullhd /boot/grub2/themes'])

print("\033[1;97m",' You must set the theme in your GRUB config file,')
while True:
	y = '  Would you like to do it now? [y/n] '
	answer = input(y)
	if answer != 'y' and 'n':
		print('  You didn\'t give a valid option, try again.')
	else:
		if answer == y:
			if Folder('/boot/grub') == True:
				if File() == True:
					

