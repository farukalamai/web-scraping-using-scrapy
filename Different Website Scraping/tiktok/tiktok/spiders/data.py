import scrapy
import json
import time
import random

class DataSpider(scrapy.Spider):
    name = 'data'
    allowed_domains = ['tiktok.com']
    start_urls = ['http://tiktok.com/']
    
    time.sleep(20)

    def parse(self, response):
        pass
