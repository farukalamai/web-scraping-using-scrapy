import scrapy
import json
import time
import random



class ProductSpider(scrapy.Spider):
    name = 'product'
    allowed_domains = ['7dollar.app']
    start_urls = ['https://www.7dollar.app/services/public/products/page/0/28/DEFAULT/en/7']

    time.sleep(20)

    def parse(self, response):
        resp = json.loads(response.body)
        products = resp.get('products')
        for product in products:
            name = product.get('description').get('name')
            img_url = product.get('image').get('imageUrl')
            price_details = product.get('productAttr')
            for price in price_details:
                box_number = price.get('name')
                price_with_box = price.get('finalPrice').get('productPrice').get('sellPriceAmount')		
            yield {
                'Name': name,
                'Image URL': img_url,
                'Box Number': box_number,
                'Price with Box': price_with_box
            }

        


