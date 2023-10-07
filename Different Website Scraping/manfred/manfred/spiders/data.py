import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DataSpider(CrawlSpider):
    name = 'data'
    allowed_domains = ['www.musikhaus-korn.de']
    start_urls = ['https://www.musikhaus-korn.de/en/electric-guitars/cd/954']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='product-list-item']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        name = response.xpath("//h1/span/text()").get()
        brand = response.xpath("//div[@class='feature']/div/a/text()").get().strip()
        model = response.xpath("(//div[@id='feature-product-model']/div/text())[2]").get().strip()
        price = response.xpath("//div/div[@id='product-price']/text()").get().strip()

        image = response.xpath("//div[1]/div[1]/div[1]/img/@src").get()

        yield {
            'Name': name,
            'Price': price,
            'Brand': brand,
            'Model': model,
            'Image': image
        }
