import scrapy
from ..items import BooksItem

class BookspyderSpider(scrapy.Spider):
    name = "bookspyder"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):

        citas = response.css('div.quote')
        for cita in citas:
            tags = cita.css('div.tags a.tag::attr(href)').getall()
            if "/tag/inspirational/page/1/" in tags:
                book_item = BooksItem()
                book_item['cita_text'] = cita.css('span.text::text').get()
                book_item['author'] = cita.css('small.author::text').get()
                yield book_item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)