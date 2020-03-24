import scrapy

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
        title = response.css('h2::text')[0].extract()
        print(title)