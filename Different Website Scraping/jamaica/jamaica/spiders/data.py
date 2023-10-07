
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DataSpider(CrawlSpider):
    name = 'data'
    allowed_domains = ['storetodoorja.com']
    start_urls = ['https://storetodoorja.com/product-category/rice-grains-pasta-beans']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        name = response.xpath("//h1/text()").get()
        price = response.xpath("//p/span[@class='woocommerce-Price-amount amount']/text()").get()
        sku = response.xpath("//span[@class='sku']/text()").get()
        category = response.xpath("//span[@class='posted_in']/a/text()").get()
        photo = response.xpath("//figure/div/a/@href").get()
        yield {
            'Name': name,
            'Price': price,
            'SKU': sku,
            'Category': category,
            'Photo': photo
        }
