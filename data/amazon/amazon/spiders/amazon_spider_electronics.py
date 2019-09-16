import scrapy
from ..items import AmazonItem


class AmazonSpiderElectronics(scrapy.Spider):
    name = 'amazon_spider_electronics'

    # start_urls = [
    #     'https://www.amazon.com/s?i=electronics-intl-ship&rh=n%3A%2116225009011&page=2&qid=1568625454&ref=lp_16225009011_pg_27'
    # ]
    start_urls= ['https://www.amazon.com/s?rh=n%3A16225009011&page=55']

    def parse(self, response):
        items = AmazonItem()
        next_page_real = response.css(".a-last a").css("::attr(href)").get()

        ad = response.css('.a-color-base.a-text-normal::text').extract()

        for i in range(len(ad)):
            items['ad'] = ad[i]

            yield items

        if next_page_real is not None:
            yield response.follow(next_page_real, callback=self.parse)
