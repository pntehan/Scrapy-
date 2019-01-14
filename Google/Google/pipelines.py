# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem

class GooglePipeline(object):
    def process_item(self, item, spider):
        return item

class ImagePipeline(ImagesPipeline):
	"""docstring for ImagePipeline"""
	def get_media_requests(self, item, info):
		yield scrapy.Request(item['image_url'])

	def item_completed(self, results, item, info):
		image_path = [x['path'] for ok, x in results if ok]
		if not image_path:
			raise DropItem("图片地址无效!")
		item['image_path'] = image_path
		return item
		
