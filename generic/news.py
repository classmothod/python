# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
	name = 'news'
	allowed_domains = ["portaldobitcoin.com"]
	start_urls = ['https://portaldobitcoin.com/']

	def ReturnValue(self, Titles, Links, DoubleD=False, One=True, Two=False, Double=False):
		Dict = {}

		if DoubleD == True:
			for y in range(len(Titles)):
				Dict[Titles[y]] = Links[y]
			File = open('/home/unsize/Documents/MiningEmotion/News.txt', 'w')
			File.write(str(Dict))
			File.close()
			return Dict

		elif One == True:
			File = open('/home/unsize/Documents/MiningEmotion/News/News.txt', 'w')
			for y in Titles:
				y = y+'\n'
				File.write(y)
			File.close()
			return Titles

		elif Two == True:
			File = open('/home/unsize/Documents/MiningEmotion/News.txt', 'w')
			for y in Links:
				y = y+'\n'
				File.write(y)
			File.close()
			return Links

		elif Double == True:
			File = open('/home/unsize/Documents/MiningEmotion/News.txt', 'w')
			for y in range(len(Titles)):
				TempT = Titles[y]+'\n'
				File.write(TempT)
				TempH = Links[y]+'\n'
				File.write(TempH)
			File.close()

	def parse(self, response):
		DivNews = response.xpath('//div[contains(@class, "wpb_wrapper")]')

		News = response.xpath('.//h3/a')
		title = News.xpath('./text()').extract()
		href = News.xpath('./@href').extract()

		self.ReturnValue(title, href)
		#yield scrapy.Request(url=url, callback=self.parse_detail)
