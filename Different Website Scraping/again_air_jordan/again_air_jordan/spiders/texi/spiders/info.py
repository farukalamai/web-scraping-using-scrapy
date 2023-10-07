import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import csv

class InfoSpider(CrawlSpider):
    name = 'info'
    allowed_domains = ['taxi-heute.de']
    start_urls = ['https://www.taxi-heute.de/de/adressen/kategorien/955']

    # def remove_characters(self, value):
    #     return value.strip('\xa0')
    


    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='views-field views-field-field-adresse-bild']/div/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        
        yield {
            'Name': response.xpath("//div[1]/div/div/div/div/div[1]/div/div[2]/h1/text()").get().strip(),
            'Street Address': response.xpath("//div/div[1]/div/fieldset[1]/div/div[1]/div[2]/text()").get(),
            'Zip Code': response.xpath("//div[1]/div/fieldset[1]/div/div[2]/div[2]/text()").get(),
            'State': response.xpath("//div[1]/div/fieldset[1]/div/div[3]/div[2]/text()").get(),
            'Phone': response.xpath("//div[1]/div/fieldset[2]/div/div[2]/div[2]/div/text()").get(),
            'Fax': response.xpath("//div[1]/div/fieldset[2]/div/div[3]/div[2]/div/text()").get(),
            'Email': response.xpath("//div[1]/div/div[1]/div/fieldset[2]/div/div[4]/div[2]/div/text()").get(),
            'Website': response.xpath("//div[1]/div/fieldset[3]/div/div/div[2]/div/a/@href").get(),
            'Category': response.xpath("//div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/div[2]/a/text()").get()
        }
