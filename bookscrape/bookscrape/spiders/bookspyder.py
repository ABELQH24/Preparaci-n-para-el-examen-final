import scrapy


class BookspyderSpider(scrapy.Spider):
    name = "bookspyder"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        pass
