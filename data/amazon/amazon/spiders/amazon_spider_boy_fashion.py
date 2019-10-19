import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderBoyFashion(scrapy.Spider):
    name = 'amazon_spider_boy'

    # start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A3455641&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A1288606011&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_2']
    # start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A5604815011&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_3']
    # start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A1046120&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_4']
    # start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A1045910&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A3455421&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_6']
    # start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A1045904&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_7']
    # start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A1045906&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_8']
    # start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A3455651&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_9']
    # start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A1046030&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_10']
    # start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A699914011&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_11']
    # start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A3455451&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_12']
    # start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A3455631&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_13']
    # start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A2422483011&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_14']
    start_urls = ['https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A16225021011%2Cn%3A1040666%2Cn%3A1046028&dc&pf_rd_i=16225021011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_p=9b25e25c-9d57-4900-b288-95d6b1ed8fc8&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_r=BFA9TJZ3XCYTX8N609H0&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571500510&rnid=1040666&ref=sr_nr_n_15']







    def parse(self, response):
        items = AmazonItem()

        next_page_real = response.css(".a-last a").css("::attr(href)").get()

        ad = response.css('.a-size-base-plus::text').extract()

        for i in range(len(ad)):
            items['ad'] = ad[i]
            yield items

        if next_page_real is not None:
            time.sleep(2)
            yield response.follow(next_page_real, callback=self.parse)