import configparser, os.path
from utils import Construct, Processing



class Configuration:

	@staticmethod
	def Initialize():
		config = configparser.ConfigParser()
		config['DEFAULT'] = {
			'directory': './List/List_tools.txt',
			'tools': './tools.ini'
		}
		config['config.user'] = {}
		config['config.user']['directory'] = './List/List_tools.txt'

		with open('init/config.ini', 'w') as configfile:
			config.write(configfile)

		if os.path.exists(config['DEFAULT']['tools']) == True:
			print('Error: file tools.ini not exists.')
			exit()

	@staticmethod
	def tools_init():
		tools = Processing()
		config = configparser.ConfigParser()
		for tool in tools:
			Name = tool[0].split(':')[1].replace(' ','')
			Description = tool[1].split(':')[1].replace('\'','')
			Description = Description.replace('\"', '-')
			Link = tool[2].split(' ')[1]
			if '%' in Link: Link = ''
			Class = tool[3].split(':')[1]
			config[Name] = {'Description':Description,'Link':Link,'Class':Class}
		
		with open('init/tools.ini', 'w', encoding='utf-8') as configfile:
			config.write(configfile)
