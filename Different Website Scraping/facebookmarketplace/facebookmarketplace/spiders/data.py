import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DataSpider(CrawlSpider):
    name = 'data'
    allowed_domains = ['facebook.com']
    start_urls = ['https://web.facebook.com/marketplace/107202002644907/search/?query=laptop']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='a75w6hnp']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        name = response.xpath("//div/span[@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf exr7barw b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas thx2cq4v hxfwr5lz qntmu8s7 tq4zoyjo o48pnaf2 pbevjfx6']/text()").get()
        price = response.xpath("//div/span[@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf exr7barw b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas m2nijcs8 szxhu1pg hpj0pwwo sggt6rq5 tpi2lg9u pbevjfx6']/text()").get()
        photo = response.xpath("//span[@class='alzwoclg b0ur3jhr']/div/img/@src").get()
        description = response.xpath("//div[@class='n3t5jt4f nch0832m rj2hsocd oxkhqvkx s1m0hq7j']/div/span[@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf exr7barw b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas m2nijcs8 hxfwr5lz k1z55t6l oog5qr5w tes86rjd pbevjfx6']/text()").get()
        location = response.xpath("//div/div[@class='alzwoclg cqf1kptm siwo0mpr gu5uzgus']/div[@class='jroqu855 nthtkgg5']/span/span[@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf exr7barw k1z55t6l oog5qr5w innypi6y pbevjfx6']/text()").get()
        
        yield {
            'Name': name,
            'Price': price,
            'Photo': photo,
            'Description': description,
            'Location': location
        }




