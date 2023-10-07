import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DataSpider(CrawlSpider):
    name = 'data'
    allowed_domains = ['thebluebook.com']
    start_urls = ['https://www.thebluebook.com/search.html?region=4&class=2200&page=3']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        name = response.xpath("//h1[@class='mt-0 mb-1']/text()[2]").get().replace("\r\n\t\t\t\t\t\t", "").replace("\r\n\t\t\t\t\t", "")
        phone = response.xpath("(//span[@class='phoneDisp']/text())[1]").get()
        website = response.xpath("//a[@id='proViewHdrWebBtn']/@href").get()
        street_address = response.xpath("(//div[@class='col-md']/div/text())[1]").get()
        state_zip = response.xpath("(//div[@class='col-md']/div/text())[2]").get()
        yield {
            'Name': name,
            'Phone': phone,
            'Website': website,
            'Street Address': street_address,
            'State and Zip': state_zip
        }
