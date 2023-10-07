import scrapy
from scrapy_selenium import SeleniumRequest



class LifestlyleSpider(scrapy.Spider):
    name = 'lifestlyle'
    
    def start_requests(self):
        yield SeleniumRequest(
            url = 'https://www.spinneyslebanon.com/lifestyle/vegeterian/',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        products = response.xpath("//ol/li[@class='item product product-item']")
        for product in products:
            link = product.xpath("normalize-space(.//a[@class='product-item-link']/@href)").get()
            name = product.xpath("normalize-space(.//a[@class='product-item-link']/text())").get()
            weight_num = product.xpath("normalize-space(.//span[@class='weight_number']/text())").get()
            weight_uniq = product.xpath("normalize-space(.//span[@class='prod_weight']/text())").get()
            price = product.xpath("normalize-space(.//span[@class='price']/text())").get()
            store_by = product.xpath("normalize-space(.//span[@class='prod_brand']/a/text())").get()

            yield {
                'Product Link': link,
                'Name': name,
                'Weight': weight_num,
                'Weight Unique': weight_uniq,
                'Price': price,
                'Store By': store_by
            }
        
        next_page = response.xpath("((//a[@class='action  next']/@href)[2]").get()
        if next_page:
            absolute_url = next_page
            yield SeleniumRequest(
                url=absolute_url,
                wait_time=3,
                callback=self.parse
            )


