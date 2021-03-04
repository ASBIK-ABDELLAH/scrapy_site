import requests
from scrapy import Selector
import scrapy
from  ..items import QuotetutorialItem

class Spider(scrapy.Spider):
    name = 'Jumia'
    page = 2
    start_urls = [
        'https://www.jumia.ma/sport-fitness-musculation/?gender=Femmes'
    ]

    def parse(self, response):
        items = QuotetutorialItem()
        div = response.css('.info')
        for quote in div:

            items['product'] = quote.css('.name::text').extract()
            items['price'] = quote.css('.prc::text').extract()
            items['stars'] = quote.css('._s::text').extract()
            items['sells'] = quote.css('.rev::text').extract()

            #enter = response.css('article.prd._fb.col.c-prd a::attr(href)').get()
            #page2= 'https://www.jumia.ma/'+str(enter)
            #response_2 = requests.get(page2)
            #tree = html.fromstring(response2.content)
            #response2= Selector(response_2)
            #items['product_information'] = response2.css("ul.-pvs.-mvxs.-phm.-lsn").extract()

            yield items

        next_page = 'https://www.jumia.ma/sport-fitness-musculation/?gender=Femmes&page='+str(Spider.page)+'#catalog-listing'
        if Spider.page < 2:
            Spider.page += 1
            yield response.follow(next_page, callback=self.parse)







