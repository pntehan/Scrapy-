# -*- coding: utf-8 -*-
import scrapy
import json
from Google.items import GoogleItem

class GoogleSpiderSpider(scrapy.Spider):
    name = 'google_spider'
    allowed_domains = ['www.duitang.com']
    start_urls = ['https://www.duitang.com/album/?id=92298633']

    def parse(self, response):
    	print(response.xpath("//div[@id='content']/div[@class='album-content']/div[1]/div[2]/div[2]").extract())
    	'''
    	if content:
    		img['image_url'] = content.xpath('.//@src').extract()
    		img['image_name'] = content.xpath('.//@alt').extract()
    		yield img
    	else:
    		print("Eorrer!")
    	'''