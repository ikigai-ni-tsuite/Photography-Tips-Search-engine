import scrapy
from urllib.parse import urlencode
from ..items import EventscrapeItem
API_KEY = "1208de1b-9d3a-435f-a41c-df151ef7cfd1"


def get_scrapeops_url(url):
    payload = {'api_key': API_KEY, 'url': url, 'bypass': 'cloudflare'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

class Website1Spider(scrapy.Spider):
    name = "website1"
    allowed_domains = ["zuerich.com"]
    start_url = "https://www.zuerich.com/en/events-zurich-and-the-region"


    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
        # yield scrapy.Request(url=get_scrapeops_url(self.start_urls[0]), callback=self.parse)
        yield scrapy.Request(url=self.start_url, headers=headers, callback=self.parse_main)

    def parse_main(self, response):
        pass
