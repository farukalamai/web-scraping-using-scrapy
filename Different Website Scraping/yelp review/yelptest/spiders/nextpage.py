import scrapy
import json
import time
import random

class NextpageSpider(scrapy.Spider):
    name = 'nextpage'
    allowed_domains = ['yelp.com']
    start_urls = [
        'https://www.yelp.com/biz/Xidi-nSMAL9LfezOpnLAlw/review_feed?rl=en&q=&sort_by=relevance_desc&start=10'
    ]

    def parse(self, response):
        resp = json.loads(response.body)
        reviews = resp.get('reviews')
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
        # # time.sleep(15)
        # next = resp.get('bizDetailsPageProps').get('reviewFeedQueryProps').get('pagination')
        # next_add = next.get('startResult')
        # last = next.get('totalResults')
        # if next_add < last:
        #     next_page_number = next_add + 10
        #     yield scrapy.Request(
        #         url=f'https://www.yelp.com/biz/TljiUnO5i-9_iH5x-mWZ7A/review_feed?rl=en&q=&sort_by=relevance_desc&start={next_page_number}',
        #         callback=self.parse
        #     )
        
        



