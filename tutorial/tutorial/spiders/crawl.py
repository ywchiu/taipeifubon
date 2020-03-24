import scrapy
from datetime import datetime
from tutorial.items import MoneyItem
class MoneyCrawler(scrapy.Spider):
    name = "money"
    start_urls = ['https://money.udn.com/rank/newest/1001/0/1']
    def parse(self, response):
        for tr in response.css('#ranking_table tr'):
            if tr.css('td'):
                url = tr.css('a::attr(href)')[0].extract()
                print(url)
                yield scrapy.Request(url, self.parse_detail)
                
    def parse_detail(self, response):
        moneyitem = MoneyItem()
        # 抓取標題
        moneyitem['title'] = response.css('h2::text')[0].extract()
        # 抓取摘要
        moneyitem['contents'] = ' '.join([e.extract() for e in response.css('#article_body p::text')])
        # 抓取時間
        dt = response.css('.shareBar__info--author span::text')[0].extract()
        moneyitem['dt'] = datetime.strptime(dt, '%Y-%m-%d %H:%M')
        #抓取類別
        moneyitem['category'] = response.css('#nav a::text')[-1].extract()
        #抓取連結
        moneyitem['url'] = response.request.url
        return moneyitem
