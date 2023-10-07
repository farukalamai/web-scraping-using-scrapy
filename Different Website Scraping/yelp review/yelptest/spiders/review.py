import scrapy
import json
import time
import random

class ReviewSpider(scrapy.Spider):
    name = 'review'
    allowed_domains = ['yelp.com']
    start_urls = [
        'https://www.yelp.com/biz/Xidi-nSMAL9LfezOpnLAlw/props'
    ]
    time.sleep(20)

    def parse(self, response):
        resp = json.loads(response.body)
        reviews = resp.get('bizDetailsPageProps').get('reviewFeedQueryProps').get('reviews')
        for review in reviews:
            time.sleep(random.randint(1,2))
            rating = review.get('rating')
            date = review.get('localizedDate')
            rev_text = review.get('comment').get('text').replace("<br><br>"," ").replace("<br>", " ").replace("\xa0", "").replace("amp;", "").replace("&#39;", "'")
            yield {
                'Rating': rating,
                'Date': date, 
                'Review Text': rev_text
            }
        

