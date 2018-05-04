from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from myproject.items import Headline

class NewsCrawlSpider(CrawlSpider):
    name = 'news_crawl'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['http://news.yahoo.co.jp/']

    rules = (
        # トピックスのページへのリンクをたどり、レスポンスをparse_topicsメソッドで処理
        Rule(LinkExtractor(allow=r'/pickup/\d+$'), callback='parse_topics'),
    )

    # def parse(self, response):
    #     for url in response.css('ul.topics a::attr("href")').re(r'/pickup/\d+$'):
    #         yield scrapy.Request(response.urljoin(url), self.parse_topics)

    def parse_topics(self, response):
        # トピックスのページからタイトルと本文を抜き出す
        item = Headline()
        item['title'] = response.css('.newsTitle ::text').extract_first()
        item['body'] = response.css('.hbody').xpath('string()').extract_first()
        yield item
