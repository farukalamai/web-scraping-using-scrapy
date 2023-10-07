import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time


class DataSpider(CrawlSpider):
    name = 'data'
    allowed_domains = ['detelefoongids.nl']
    start_urls = [
        'https://www.detelefoongids.nl/dietist/4-1/?page=31',
        'https://www.detelefoongids.nl/dietist/4-1/?page=32',
        'https://www.detelefoongids.nl/dietist/4-1/?page=33',
        'https://www.detelefoongids.nl/dietist/4-1/?page=34',
        'https://www.detelefoongids.nl/dietist/4-1/?page=35',
        'https://www.detelefoongids.nl/dietist/4-1/?page=36',
        'https://www.detelefoongids.nl/dietist/4-1/?page=37',
        'https://www.detelefoongids.nl/dietist/4-1/?page=38',
        'https://www.detelefoongids.nl/dietist/4-1/?page=39',
        'https://www.detelefoongids.nl/dietist/4-1/?page=40',
        'https://www.detelefoongids.nl/dietist/4-1/?page=41',
        'https://www.detelefoongids.nl/dietist/4-1/?page=42',
        'https://www.detelefoongids.nl/dietist/4-1/?page=43',
        'https://www.detelefoongids.nl/dietist/4-1/?page=44',
        'https://www.detelefoongids.nl/dietist/4-1/?page=45',
        'https://www.detelefoongids.nl/dietist/4-1/?page=46',
        'https://www.detelefoongids.nl/dietist/4-1/?page=47',
        'https://www.detelefoongids.nl/dietist/4-1/?page=48',
        'https://www.detelefoongids.nl/dietist/4-1/?page=49',
        'https://www.detelefoongids.nl/dietist/4-1/?page=50',
        'https://www.detelefoongids.nl/dietist/4-1/?page=51',
        'https://www.detelefoongids.nl/dietist/4-1/?page=52'
    ]

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div/h2/span/a"), callback='parse_item', follow=True),
    )
    time.sleep(1)

    def parse_item(self, response):
        time.sleep(2)
        dietist_url = response.xpath("//link[@rel='canonical']/@href").get()
        name = response.xpath("(//h1/span/text())[1]").get()
        city = response.xpath("(//h1/span/text())[2]").get().replace("in ", "")
        phone = response.xpath("(//span[@itemprop='telephone']/text())[1]").get()
        website = response.xpath("//ul/div/p/a/@href").get()

        yield {
            'Dietist Url': dietist_url,
            'Company Name': name,
            'City': city,
            'Phone': phone,
            'Website': website
        }
