# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
import os
import shutil

class DemoPipeline(object):
    def process_item(self, item, spider):
        return item

class My_imagePipeline(ImagesPipeline):
    #image_store = "C:/Users/Administrator/Desktop/Scrapydemo/demo/image/full/"
    img_store = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        if item['image_url'] == None:
            pass
        else:
            yield scrapy.Request(item['image_url'])

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem("图片地址无效!")
        name = item['image_name'].split('(')[0]
        if len(item['image_name'].split('(')) == 1:
            num = '1'
        else:
            num = item['image_name'].split('(')[1].split(')')[0]
        img_path = "%s/%s"%(self.img_store, name)
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        try:
            shutil.move(self.img_store+'/'+image_path[0], img_path+'/'+num+'.jpg')
        except:
            pass
        item['image_path'] = img_path + '/' + num + '.jpg'
        return item
