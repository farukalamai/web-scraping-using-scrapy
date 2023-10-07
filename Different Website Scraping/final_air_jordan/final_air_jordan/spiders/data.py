
import scrapy
import json
import time
import random


class DataSpider(scrapy.Spider):
    name = 'data'
    
    headers = {
        "authority": "wethenew.com",
        "path": "/products/air-jordan-1-mid-diamond-shorts.json",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "referer": "https://wethenew.com/products/air-jordan-1-mid-diamond-shorts",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    def parse(self, response):
        url = 'https://wethenew.com/products/air-jordan-1-mid-diamond-shorts.json'

        request = scrapy.Request(
            url,
            callback=self.parse_api,
            headers=self.headers
        )
        yield request
    
    def parse_api(self, response):
        raw_data = response.body
        data = json.loads(raw_data)
        name = data.get('product')
        yield {
            'Name': name
        }




