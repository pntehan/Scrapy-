import scrapy
from tutorial.items import DemoItem

class demo_spider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        'https://movie.douban.com/top250'
    ]
    def parse(self, response):
        info = DemoItem()
        movies = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for movie in movies:
            info['movie_number'] = movie.xpath(".//div[@class='item']//em/text()").extract_first()
            info['movie_name'] = movie.xpath(".//div[@class='info']//a/span[1]/text()").extract_first()
            content = movie.xpath(".//div[@class='info']//p[1]/text()").extract()
            for i in content:
                info['movie_info'] = "".join(i.split())
            info['movie_star'] = movie.xpath(".//div[@class='info']//div[@class='star']/span[2]/text()").extract_first()
            info['movie_describ'] = movie.xpath(".//div[@class='info']//p[@class='quote']/span/text()").extract_first()
            yield info
        next_page = response.xpath("//*[@id='content']/div/div[1]/div[2]/span[3]/a/@href").extract_first()
        if next_page:
            yield scrapy.Request("https://movie.douban.com/top250"+next_page, callback=self.parse)



