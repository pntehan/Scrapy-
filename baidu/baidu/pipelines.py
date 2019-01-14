# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import scrapy


class BaiduPipeline(object):
    def process_item(self, item, spider):
        return item

class BaiduImagePipeline(ImagesPipeline):
	"""docstring for ImagePipeline"""
	
	def get_media_requests(self, item, info):
		for i in item['image_urls']:
			yield scrapy.Request(i)

	def item_completed(self, results, item, info):
		image_paths = [x['path'] for ok, x in results if ok]
		if not image_paths:
			raise DropItem("图片地址失效！")
		item['image_paths'] = image_paths
		return item


