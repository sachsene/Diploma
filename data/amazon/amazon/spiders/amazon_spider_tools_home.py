import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderToolsHome(scrapy.Spider):
    name = 'amazon_spider_tools'

    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A19149191011&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741261&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_2']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741271&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_3']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741331&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_4']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A13399891&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741441&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_7']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741411&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_8']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741161&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_9']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741361&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_10']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A2383576011&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_13']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741521&dc&fst=as%3Aoff&qid=1571596356&rnid=13397451&ref=sr_nr_n_14']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A468240%2Cn%3A551240%2Cn%3A13397641&dc&page=356&fst=as%3Aoff&qid=1571598103&rnid=551240&ref=sr_pg_356']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A551240%2Cn%3A495346&dc&fst=as%3Aoff&qid=1571600524&rnid=551240&ref=sr_nr_n_2']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A551240%2Cn%3A553504&dc&fst=as%3Aoff&qid=1571645836&rnid=551240&ref=sr_nr_n_3']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A551240%2Cn%3A553470&dc&fst=as%3Aoff&qid=1571645836&rnid=551240&ref=sr_nr_n_4']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A468240%2Cn%3A551240%2Cn%3A553516&dc&page=317&fst=as%3Aoff&qid=1571649454&rnid=551240&ref=sr_pg_317']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A551240%2Cn%3A553490&dc&fst=as%3Aoff&qid=1571645836&rnid=551240&ref=sr_nr_n_6']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A5789850011&dc&fst=as%3Aoff&qid=1571856754&rnid=495266&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A468240%2Cn%3A495266%2Cn%3A6369357011&dc&page=288&fst=as%3Aoff&qid=1571858216&rnid=495266&ref=sr_pg_288']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=2566430111&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A11042051&dc&fst=as%3Aoff&qid=1571856754&rnid=495266&ref=sr_nr_n_3']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A6396121011&dc&fst=as%3Aoff&qid=1571856754&rnid=495266&ref=sr_nr_n_4']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A495320&dc&fst=as%3Aoff&qid=1571856754&rnid=495266&ref=sr_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A6369359011&dc&fst=as%3Aoff&qid=1571856754&rnid=495266&ref=sr_nr_n_6']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A6426213011&dc&fst=as%3Aoff&qid=1571856754&rnid=495266&ref=sr_nr_n_7']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A495310&dc&fst=as%3Aoff&qid=1571856754&rnid=495266&ref=sr_nr_n_8']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A468240%2Cn%3A495266%2Cn%3A3753381&dc&page=350&fst=as%3Aoff&qid=1571905621&rnid=495266&ref=sr_pg_350']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A6478739011&dc&fst=as%3Aoff&qid=1571905784&rnid=495266&ref=sr_nr_n_10']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A14328101&dc&fst=as%3Aoff&qid=1571904172&rnid=495266&ref=sr_nr_n_11']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A495334&dc&fst=as%3Aoff&qid=1571904172&rnid=495266&ref=sr_nr_n_12']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A468240%2Cn%3A495266%2Cn%3A495334&dc&page=188&fst=as%3Aoff&qid=1571915840&rnid=495266&ref=sr_pg_188']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A6396120011&dc&fst=as%3Aoff&qid=1571904172&rnid=495266&ref=sr_nr_n_13']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A17854127011&dc&fst=as%3Aoff&qid=1571904172&rnid=495266&ref=sr_nr_n_14']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A3736711&dc&fst=as%3Aoff&qid=1571904172&rnid=495266&ref=sr_nr_n_15']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A468240%2Cn%3A495266%2Cn%3A495324&dc&page=304&fst=as%3Aoff&qid=1571933926&rnid=495266&ref=sr_pg_304']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A468240%2Cn%3A495266%2Cn%3A306719011&dc&page=357&fst=as%3Aoff&qid=1571952839&rnid=495266&ref=sr_pg_357']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A495336&dc&fst=as%3Aoff&qid=1571930069&rnid=495266&ref=sr_nr_n_18']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A495340&dc&fst=as%3Aoff&qid=1571930069&rnid=495266&ref=sr_nr_n_19']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A495266%2Cn%3A6396126011&dc&fst=as%3Aoff&qid=1571930069&rnid=495266&ref=sr_nr_n_20']
    start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A468240%2Cn%3A495266%2Cn%3A6497674011&dc&page=371&fst=as%3Aoff&qid=1571959277&rnid=495266&ref=sr_pg_371']










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