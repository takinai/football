# ライブラリ設定
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from myproject.items import Table

# サッカー勝敗データのクローリング
class FootballCrawlSpider(CrawlSpider):
    name = 'football_crawl'
    allowed_domains = ['soccer.from.tv']
    # start_urls = ['http://soccer.from.tv/match']

    # テスト用
    start_urls = ['http://soccer.from.tv/team/294/y18/']

    rules = (
        # トピックスのページへのリンクをたどり、レスポンスをparse_topicsメソッドで処理
        # \d：アラビア数字
        # +：直前の表現が1個以上存在
        # $：行の最後にマッチする
        Rule(LinkExtractor(allow=r'/team/\d{1,4}/y\d+/'), callback='parse_result'),

        # 以下本番
        # Rule(LinkExtractor(allow=r'/team/\d{1,4}/',
        #                    deny=(r'/team/\d{1,4}/\d{1,4}/',
        #                          r'/team/\d{1,4}/summary',
        #                          r'/team/\d{1,4}/y\d+/\w+/',
        #                          r'/team/\d{1,4}/all/',
        #                          r'/team/\d{1,4}/all/\w+/'))),
        # Rule(LinkExtractor(allow=r'/team/\d{1,4}/y\d+/',
        #                    deny=r'/team/\d{1,4}/y\d+/\w+/'),
        #      callback='parse_topics'),
    )

    def parse_result(self, response):
        item = Table()

        # 自チーム名の抽出
        item['team'] = response.css('div#main-column div.page_title b::text').extract_first()

        # 試合結果の項目名の抽出
        item['key'] = response.css('div#main-column table.tb1 th::text').extract()

        # 試合結果の内容の抽出
        item['value'] = response.css('div#main-column table.tb1 td::text').extract()

        yield item

# 以下をターミナルで実行することで、json line形式でファイルアウトプット
# 本当はmysqlに直接つなぎたい
# scrapy runspider scr_v003.py -o scr_result.jl

# 以下参考
# scrapy shell http://soccer.from.tv/team/294/y18/
#     response.text
