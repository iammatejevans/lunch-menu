import scrapy


class NaKopeckuSpider(scrapy.Spider):
    name = 'na_kopecku'

    def start_request(self):
        url = 'https://www.restaurace-nakopecku.cz/tydenni-poledni-nabidka/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        days = response.css('.dm-name').getall()
        print('hovno')
        
