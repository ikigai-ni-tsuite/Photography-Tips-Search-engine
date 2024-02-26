import scrapy


class Website1Spider(scrapy.Spider):
    name = "website1"
    allowed_domains = ["zuerich.com"]
    start_urls = ["https://www.zuerich.com/en/events-zurich-and-the-region"]

    def parse(self, response):
        
