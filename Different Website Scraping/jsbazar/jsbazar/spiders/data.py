import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DataSpider(CrawlSpider):
    name = 'data'
    allowed_domains = ['laptopbatteryexpress.com']
    start_urls = ['https://www.laptopbatteryexpress.com/Acer-laptop-batteries-s/78.htm']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='v-product__details']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'name': response.xpath("//font[@class='productnamecolorLARGE colors_productname']/span/text()").get(),
            'price': response.xpath("//span[@itemprop='price']/text()").get(),
            'image': response.xpath("//a[@id='product_photo_zoom_url']/@href").get(),
            'name': response.xpath("(//h1/text())[1]").get(),
            'part_number': response.xpath("(//div[@class='ymq-tab-content-item ymq-tab-content-item-active']/div/p/text())[1]").get(),
            'model_number': response.xpath("(//div[@class='ymq-tab-content-item ymq-tab-content-item-active']/div/p/text())[3]").get()
        }
