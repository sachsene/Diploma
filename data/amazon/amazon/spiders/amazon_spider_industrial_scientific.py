import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderIndustrialScientific(scrapy.Spider):
    name = 'amazon_spider_industrial'

    # start_urls = ['https://www.amazon.com/s?i=industrial-intl-ship&rh=n%3A%2116225012011&page=2&qid=1568990497&ref=lp_16225012011_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=industrial-intl-ship&bbn=16225012011&rh=n%3A16225012011%2Cn%3A256167011&dc&page=2&fst=as%3Aoff&qid=1570208823&rnid=16225012011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=industrial-intl-ship&bbn=16225012011&rh=n%3A16225012011%2Cn%3A6066126011&dc&page=318&fst=as%3Aoff&qid=1570217506&rnid=16225012011&ref=sr_pg_318']
    # start_urls = ['https://www.amazon.com/s?i=industrial-intl-ship&bbn=16225012011&rh=n%3A16225012011%2Cn%3A256225011&dc&page=370&fst=as%3Aoff&qid=1570228643&rnid=16225012011&ref=sr_pg_370']
    # start_urls = ['https://www.amazon.com/s?i=industrial-intl-ship&bbn=16225012011&rh=n%3A16225012011%2Cn%3A13400231&dc&page=2&fst=as%3Aoff&qid=1570268983&rnid=16225012011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=industrial-intl-ship&bbn=16225012011&rh=n%3A16225012011%2Cn%3A10773802011&dc&page=350&fst=as%3Aoff&qid=1570272653&rnid=16225012011&ref=sr_pg_350']
    # start_urls = ['https://www.amazon.com/s?i=industrial-intl-ship&bbn=16225012011&rh=n%3A16225012011%2Cn%3A5772192011&dc&page=2&fst=as%3Aoff&qid=1570273036&rnid=16225012011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=industrial-intl-ship&bbn=16225012011&rh=n%3A16225012011%2Cn%3A383598011&dc&page=261&fst=as%3Aoff&qid=1570291687&rnid=16225012011&ref=sr_pg_261']
    # start_urls = ['https://www.amazon.com/s?i=industrial-intl-ship&bbn=16225012011&rh=n%3A%2116225012011%2Cn%3A18746931011&dc&fst=as%3Aoff&qid=1570265229&rnid=16225012011&ref=lp_16225012011_nr_n_7']
    # start_urls = ['https://www.amazon.com/s?i=industrial-intl-ship&bbn=16225012011&rh=n%3A16225012011%2Cn%3A383599011&dc&page=2&fst=as%3Aoff&qid=1570292821&rnid=16225012011&ref=sr_pg_2']
    start_urls = ['https://www.amazon.com/s?i=industrial-intl-ship&bbn=16225012011&rh=n%3A16225012011%2Cn%3A3061625011&dc&page=290&fst=as%3Aoff&qid=1570297358&rnid=16225012011&ref=sr_pg_290']

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
