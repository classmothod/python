# -*- coding: utf-8 -*-
import scrapy


class ToolsSpider(scrapy.Spider):
    name = 'tools'
    allowed_domains = 'blackarch.org'
    start_urls = 'https://blackarch.org/tools.html'

    def parse(self, response):
        trs = response.xpath('/html/body/div/div[3]/div[2]/table/tbody/tr')
        for td in trs:
        	Name_tool = td.xpath('td[contains(@class, "tbl-name")]/text()').extract_first()
        	Description = td.xpath('td[3]/text()').extract_first()
        	Class_tool = td.xpath('td[4]/a/text()').extract_first()
        	Link_tool = td.xpath('td[5]/a/@href').extract_first()
        	self.log(Name_tool, Link_tool)

'''
for td in trs:
Name_tool = td.xpath('td[contains(@class, "tbl-name")]/text()').extract_first()
Description = td.xpath('td[3]/text()').extract_first()
Link_tool = td.xpath('td[5]/a/@href').extract_first()
Class_tool = td.xpath('td[4]/a/text()').extract_first()
with open('/root/Desktop/List_tools.txt', 'a', encoding='utf-8') as File:
Text = 'Name tool: {}\nDescription: {}\nLink: {}\nClass: {}\n'.format(Name_tool, Description, Link_tool, Class_tool)
File.write(Text)
File.close()
'''