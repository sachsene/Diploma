import time

import scrapy
from ..items import AmazonItem


class AmazonSpiderElectronics(scrapy.Spider):
    name = 'amazon_spider_electronics'

    # start_urls = [
    #     'https://www.amazon.com/s?i=electronics-intl-ship&rh=n%3A%2116225009011&page=2&qid=1568625454&ref=lp_16225009011_pg_27'
    # ]
    # start_urls = ['https://www.amazon.com/s?rh=n%3A16225009011&page=175']
    # start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A281407&dc&page=2&fst=as%3Aoff&qid=1569776909&rnid=16225009011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A502394&dc&page=2&fst=as%3Aoff&qid=1569779520&rnid=16225009011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A3248684011&dc&page=2&fst=as%3Aoff&qid=1569783301&rnid=16225009011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A2811119011&dc&page=2&fst=as%3Aoff&qid=1569801647&rnid=16225009011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A172526&dc&page=2&fst=as%3Aoff&qid=1569805121&rnid=16225009011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A172541&dc&page=118&fst=as%3Aoff&qid=1569808648&rnid=16225009011&ref=sr_pg_118']
    # start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A667846011&dc&page=283&fst=as%3Aoff&qid=1569866370&rnid=16225009011&ref=sr_pg_283']
    # start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A172574&dc&page=360&fst=as%3Aoff&qid=1569869940&rnid=16225009011&ref=sr_pg_360']
    # start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A172623&dc&page=372&fst=as%3Aoff&qid=1569873531&rnid=16225009011&ref=sr_pg_372']
    # start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A524136&dc&page=370&fst=as%3Aoff&qid=1569878868&rnid=16225009011&ref=sr_pg_370']
    # start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A1266092011&dc&page=370&fst=as%3Aoff&qid=1569935643&rnid=16225009011&ref=sr_pg_370']
    # start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A7926841011&dc&page=370&fst=as%3Aoff&qid=1569944770&rnid=16225009011&ref=sr_pg_370']
    # start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A300334&dc&page=2&fst=as%3Aoff&qid=1569944956&rnid=16225009011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A10048700011&dc&page=371&fst=as%3Aoff&qid=1569949011&rnid=16225009011&ref=sr_pg_371']
    start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A2642125011&dc&page=2&fst=as%3Aoff&qid=1569950076&rnid=16225009011&ref=sr_pg_2']

    def parse(self, response):
        items = AmazonItem()
        next_page_real = response.css(".a-last a").css("::attr(href)").get()

        ad = response.css('.a-color-base.a-text-normal::text').extract()

        for i in range(len(ad)):
            items['ad'] = ad[i]
            yield items

        if next_page_real is not None:
            time.sleep(5)
            yield response.follow(next_page_real, callback=self.parse)
