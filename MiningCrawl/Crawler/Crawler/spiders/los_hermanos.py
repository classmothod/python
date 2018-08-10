# -*- coding: utf-8 -*-
import scrapy


class LosHermanosSpider(scrapy.Spider):
	name = 'los-hermanos'
	allowed_domains = ['www.letras.mus.br']
	start_urls = ['http://www.letras.mus.br/los-hermanos/discografia/4-2005/']

	def parse(self, response):
		Nome_album = response.xpath('//h4/a/text()').extract_first()
		Musics = response.xpath('//div[contains(@class, "cnt-discografia_cd")]/ol/li')

		for Music in Musics:
			url_music = Music.xpath('./a/@href').extract_first()

			yield scrapy.Request(
				url='https://www.letras.mus.br%s'%url_music,
				callback=self.parser_music
			)

	def parser_music(self, response):
		directory = '../../Date/Date_crawler/4.txt'
		
		Nome_Music = response.xpath('//div[contains(@class, "cnt-head_title")]/h1/text()').extract_first()
		Nome_Music = Nome_Music + '\n'
		Letra_Music = response.xpath('//div[contains(@class, "cnt-letra")]/article/p/text()').extract()
		
		#with open(directory, 'a') as File:
		#	File.write(Nome_Music)

		for p in Letra_Music:
			with open(directory, 'a') as File:
				text = str(p)+'\n' 
				File.write(str(text))
		
		with open(directory, 'a') as File:
			File.write('\n')