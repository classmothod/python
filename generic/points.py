import time

Frase = ['I elliot alderson | i think i found hell',
	'Running After my fate', 'Goner', 'These voices wont leave','\n']

Points = '.'
L = []

for i in range(30):
	L.append(str(Points))
	Points += '.'

for i in Frase:
	print("\033[K", i.strip(), end="\n")
	time.sleep(1)
	for y in L:
		print("\033[K", y.strip(), end="\r")
		time.sleep(0.1)
