# -*- coding: utf-8 -*-
import scrapy
import re
import json
from baidu.items import BaiduItem

class BaiduSpiderSpider(scrapy.Spider):
    name = 'baidu_spider'
    allowed_domains = ['www.aitaotu.com']
    start_urls = ['https://www.aitaotu.com/tag/tuinvlang.html']

    def parse(self, response):
        text = response.xpath("//*[@id='mainbodypul']/li")
        for i in text:
            content = 'https://www.aitaotu.com/'+i.xpath(".//a[@class='Pli-litpic']/@href").extract_first()
            yield scrapy.Request(content, callback=self.DownlordImg)
        '''
        links = response.xpath("//*[@id='pageNum']/span/a")
        for j in links:
            if j.xpath(".//text()").extract_first() == '下一页':
                next_link = 'https://www.aitaotu.com/'+j.xpath(".//@href").extract_first()
                yield scrapy.Request(next_link, callback=self.parse)
        '''

    def DownlordImg(self, response):
        img = BaiduItem()
        content = response.xpath("//*[@id='big-pic']/p/a/img")
        if content:
            img['image_urls'] = content.xpath(".//@src").extract()
            yield img
        links = response.xpath("/html/body/div[3]/div[2]/div[9]/ul/li")
        for j in links:
            if j.xpath(".//a/text()").extract_first() == '下一页':
                next_link = 'https://www.aitaotu.com/'+j.xpath(".//a/@href").extract_first()
                yield scrapy.Request(next_link, callback=self.DownlordImg)
