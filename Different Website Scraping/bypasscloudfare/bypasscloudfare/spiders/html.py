import requests
import scrapy
from bs4 import BeautifulSoup
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule




class HtmlSpider(CrawlSpider):
    name = 'html'
    allowed_domains = ['costway.com']
    start_urls = ['https://www.costway.com']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
