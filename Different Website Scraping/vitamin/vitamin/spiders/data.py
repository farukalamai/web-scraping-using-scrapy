import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time
import requests


class DataSpider(CrawlSpider):
    name = 'data'
    allowed_domains = ['vitamines.com']
    start_urls = [
        'https://vitamines.com/collageen/?page=1',
        'https://vitamines.com/collageen/?page=2',
        'https://vitamines.com/eiwitten/?page=1',
        'https://vitamines.com/eiwitten/?page=2'
    ]

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='row products']/div/div/a[1]"), callback='parse_item', follow=True),
    )
    
    def parse_item(self, response):
        time.sleep(2)
        product_url = response.xpath("//link[@rel='canonical']/@href").get()
        name = response.xpath("//h1/text()").get()


        try:
            short_description_1 = response.xpath("//div[@class='short-description']/p[1]/text()").get()
        except:
            short_description_1 = ''
        try:
            short_description_2 = response.xpath("//div[@class='short-description']/p[2]/text()").get()
        except:
            short_description_2 = ''
        try:
            short_description_3 = response.xpath("//div[@class='short-description']/p[3]/text()").get()
        except:
            short_description_3 = ''           
        


        product_usage = response.xpath("//div/div[2]/div[@class='product-tab-details']/p/text()").get()

        yield {
            'Product URL': product_url,
            'Name': name,
            'Short Description 1': short_description_1,
            'Short Description 2': short_description_2,
            'Short Description 3': short_description_3,                        
            'Product Usage': product_usage
        }
