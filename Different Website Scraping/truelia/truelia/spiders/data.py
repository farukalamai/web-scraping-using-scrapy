import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time


class DataSpider(CrawlSpider):
    name = 'data'
    allowed_domains = ['trulia.com']
    start_urls = [
        # 'https://www.trulia.com/sold/12079_c/5p_ls/'
        # 'https://www.trulia.com/sold/12079_c/5p_ls/2_p/'
        # 'https://www.trulia.com/sold/12079_c/5p_ls/3_p/'
        'https://www.trulia.com/sold/12079_c/5p_ls/4_p/'
    ]

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[1]/ul/li/div/div/div/div/div[2]/div/a"), callback='parse_item', follow=True),
    )

    time.sleep(2)

    def parse_item(self, response):
        
        url = response.xpath("//link[@rel='canonical']/@href").get()
        strt_adr = response.xpath("//h1/span[@class='Text__TextBase-sc-1cait9d-0 cncmVh']/text()").get()

        second_adr = response.xpath("//h1/span[@class='Text__TextBase-sc-1cait9d-0 iTXUhg HomeSummaryShared__CityStateAddress-sc-1oogdwk-0 eIOwCY']/text()").get()
        sub_ad = second_adr.split(",")
        city = sub_ad[0]
        st_zi = sub_ad[1].strip().split(" ")
        state = st_zi[0]
        zip_code = st_zi[1]
        last_date_sold = response.xpath("(//div/div[@class='Text__TextBase-sc-1cait9d-0-div Text__TextContainerBase-sc-1cait9d-1 csrRqu gUnlde'])[1]/text()").get()
        price = response.xpath("(//h3/div[@class='Text__TextBase-sc-1cait9d-0-div Text__TextContainerBase-sc-1cait9d-1 cikoTb gUnlde'])[1]/text()").get()
        listed = response.xpath("(//div[@class='Grid__GridContainer-sc-144isrp-1 jFarAz']/div/div[@class='Text__TextBase-sc-1cait9d-0-div Text__TextContainerBase-sc-1cait9d-1 kuUYsF gUnlde'])[last()]/text()").get()
        lot_area = response.xpath("//div[@data-testid='home-summary-size-lotsize']/text()").get()
        yield {
            'URL': url,
            'Street Address': strt_adr,
            'City': city,
            'State': state,
            'Zip': zip_code,
            'Last Sold Date': last_date_sold,
            'Price': price,
            'Listed': listed,
            'Lot Area': lot_area
        }
