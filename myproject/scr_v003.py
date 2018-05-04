from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from myproject.items import Headline

class FootballCrawlSpider(CrawlSpider):
    name = 'football_crawl'
    allowed_domains = ['soccer.from.tv']
    start_urls = ['http://soccer.from.tv/match']
    # start_urls = ['http://soccer.from.tv/team/276/']

    rules = (
        # トピックスのページへのリンクをたどり、レスポンスをparse_topicsメソッドで処理
        # \d：アラビア数字
        # +：直前の表現が1個以上存在
        # $：行の最後にマッチする
        # Rule(LinkExtractor(allow=r'/team/\d+$'), callback='parse_topics'),
        Rule(LinkExtractor(allow=r'/team/\d{1,4}/',
                           deny=(r'/team/\d{1,4}/\d{1,4}/',
                                 r'/team/\d{1,4}/summary',
                                 r'/team/\d{1,4}/y\d+/\w+/',
                                 r'/team/\d{1,4}/all/',
                                 r'/team/\d{1,4}/all/\w+/'))),
        Rule(LinkExtractor(allow=r'/team/\d{1,4}/y\d+/',
                           deny=r'/team/\d{1,4}/y\d+/\w+/'),
             callback='parse_topics'),
    )

    # def parse(self, response):
    #     for url in response.css('ul.topics a::attr("href")').re(r'/pickup/\d+$'):
    #         yield scrapy.Request(response.urljoin(url), self.parse_topics)

    def parse_topics(self, response):
        pass
        # トピックスのページからタイトルと本文を抜き出す
        # item = Headline()
        # item['title'] = response.css('.newsTitle ::text').extract_first()
        # item['body'] = response.css('.hbody').xpath('string()').extract_first()
        # yield item
