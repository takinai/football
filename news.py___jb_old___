import scrapy

class NewsSpider(scrapy.Spider):
# Spiderの名前
    name = 'news'
# クロール対象のドメインリスト
    allowed_domains = ['news.yahoo.co.jp']
# クロールを開始するURKのリスト
    start_urls = ['http://news.yahoo.co.jp/']

    def parse(self, response):
        print(response.css('ul.topics a::attr("href")').extract())
