import scrapy

class DroneSpider(scrapy.Spider):
    name = 'drones'
    allowed_domain = ['https://flycamvn.com']
    start_urls = ['https://flycamvn.com/dji-mavic-pro/']

    def parse(self, response):
        products = response.css('div.list-sp')
        for drone in products:
            items = {
                'Name' : drone.css('h3 > a::text').get(),
                'Old price' : drone.css('del::text').get(),
                'New price' : drone.css('span.gia-tot::text').get(),
                'Save' : drone.css('span.giamgia::text').get(),
                'Link' : drone.css('h3 > a::attr(href)').get() 
            }
            yield items
        next_page = response.css('a.nextpostslink::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
