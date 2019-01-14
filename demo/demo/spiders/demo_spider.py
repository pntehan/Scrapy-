# -*- coding: utf-8 -*-
import scrapy
from demo.items import DemoItem

class DemoSpiderSpider(scrapy.Spider):
    name = 'demo_spider'
    allowed_domains = ['www.ituba.cc']
    start_urls = ['https://www.ituba.cc/meinvtaotu/p1.html']

    def parse(self, response):
        content = response.xpath("//*[@id='NewList']/ul/li")
        if content:
            links = content.xpath(".//a[1]/@href").extract()
            #name = content.xpath(".//a[2]/@title").extract()
            for i in links:
                yield scrapy.Request(i, callback=self.get_imageUrl)


    def get_imageUrl(self, response):
        img = DemoItem()
        img['image_name'] = response.xpath("//*[@id='ArticlePicBox1']/p/a[1]/img/@alt").extract_first()
        img['image_url'] = response.xpath("//*[@id='ArticlePicBox1']/p/a[1]/img/@src").extract_first()
        yield img
        if response.xpath("//*[@id='nl']/a/text()").extract_first() == '下一页':
            next_link = 'https://www.ituba.cc/meinvtaotu/' + response.xpath("//*[@id='nl']/a/@href").extract_first()
            yield scrapy.Request(next_link, callback=self.get_imageUrl)




