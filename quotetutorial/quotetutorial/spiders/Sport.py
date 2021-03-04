import scrapy
from ..items import QuotetutorialItem

class Spider_all(scrapy.Spider):
    name = 'Jumia_all'
    page = 2
    start_urls = [
        'https://www.jumia.ma/sport-fitness-musculation/'
    ]

    def parse(self, response):
        items = QuotetutorialItem()
        div = response.css('.info')
        for quote in div:
            items['product'] = quote.css('.name::text').extract()
            items['price'] = quote.css('.prc::text').extract()
            items['stars'] = quote.css('._s::text').extract()
            items['sells'] = quote.css('.rev::text').extract()

            yield items

        next_page = 'https://www.jumia.ma/sport-fitness-musculation/?page='+str(Spider_all.page)+'#catalog-listing'
        if Spider_all.page < 51:
            Spider_all.page += 1
            yield response.follow(next_page, callback=self.parse)





