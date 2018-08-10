import subprocess, time

class Processing:

	def __init__(self):

		self.Musics = []
		self.MusicsProcessing = []
		self.directory = '../Date/TextProcessing/TextProcessing.py'
		self.notPhraseDouble = []

	def ReadFile(self):
		File = open('../Date/Date_crawler/4.txt', 'r')
		Text = File.readlines()
		for line in Text:
			if line != '\n':
				self.Musics.append(line.replace('\n', ''))
		File.close()
		for Phrase in self.Musics:
			if Phrase not in self.notPhraseDouble:
				self.notPhraseDouble.append(Phrase)

	def ClassFy(self):
		for line in self.notPhraseDouble:
			print(line)
			Emotion = input('Emoção: ')
			if Emotion != 'null':
				ytuple = line,Emotion
				self.MusicsProcessing.append(ytuple)

	def attBase(self):
		CMD = ['mate-terminal']
		CMD.extend(['-x','bash', '-c','cd ../Crawler/Crawler && scrapy crawl los-hermanos ; exec $SHELL'])
		subprocess.Popen(CMD, stdout=subprocess.PIPE)
		time.sleep(5)

	def WriteFile(self, Name):
		with open(self.directory, 'a') as File:
			string = 'def '+Name+'():\n    base = [\n'
			File.write(string)
		last = 1
		for line in self.MusicsProcessing:
			if last == len(self.MusicsProcessing):
				with open(self.directory, 'a') as File:
					text = '        ("' + str(line[0]) + ', ' + str(line[1]) + '")]\n'
					File.write(text)
			else:
				with open(self.directory, 'a') as File:
					text = '        ("' + str(line[0]) + ', ' + str(line[1]) + '"),\n'
					File.write(text)
			last += 1
		with open(self.directory, 'a') as File:
					text = '    return base'
					File.write(text)


if __name__ == '__main__':

	Processing = Processing()
	#user = input('Nome de usuário: ')
	user = 'unsize'
	print('\nWelcome To The Machine\n')
	temp_commands = []
	while True:
		command = input('%s@machine:~$ '%user)
		command = command.lower()

		if command == 'help':
			text = """
	attBase       Para atualizar a base de dados.
	ReadFile      Para ler frase dá base de dados.
	ClassFy       Para iniciar classificação 
				das frases que estão 
					carregadas pela função ReadFile.
	WriteFile     Para escrever classificação em um arquivo .py

			"""
			print(text)
		elif command == 'attbase':
			Processing.attBase()
			temp_commands.append('attbase')

		elif command == 'readfile':
			Processing.ReadFile()
			temp_commands.append('readfile')

		elif command == 'classfy':
			Processing.ClassFy()
			temp_commands.append('classfy')

		elif command == 'writefile':
			input_temp = input('Nome: ')
			Processing.WriteFile(input_temp)
			temp_commands.append('writefile')

		elif command == 'temp':
			print(temp_commands)

		elif command == 'quit':
			exit()

		elif command == 'notlist':
			print(Processing.notPhraseDouble)

		else:
			print('Comando não existe! \\o/')