import scrapy
from scrapy_selenium import SeleniumRequest


class SearchSpider(scrapy.Spider):
    name = 'search'

    def start_requests(self):
        yield SeleniumRequest(
            url = 'view-source:https://www.reco.on.ca/RegistrantSearch/RegistrantSearch/Salesperson',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        products = response.xpath("//div[@role='tablist']/div[@class='card mt-2']")
        for product in products:
            name = product.xpath("normalize-space(.//h4[@class='mb-0']/text())").get()
            # broker_of_record = product.xpath("normalize-space(.//a[@class='product-item-link']/text())").get()
            # broker_address = product.xpath("normalize-space(.//span[@class='weight_number']/text())").get()
            # email = product.xpath("normalize-space(.//span[@class='prod_weight']/text())").get()
            # phone = product.xpath("normalize-space(.//span[@class='price']/text())").get()
            
            yield {
                'Name': name   
            }
# 'Broker Record': broker_of_record,
                # 'Broker Address': broker_address,
                # 'Email': email,
                # 'Phone': phone