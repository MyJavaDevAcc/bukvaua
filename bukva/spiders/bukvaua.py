import scrapy


class BukvauaSpider(scrapy.Spider):
    name = 'bukvaua'
    allowed_domains = ['bukva.ua']
    start_urls = ['https://bukva.ua/ua/catalog/browse/248']
    
    def parse(self, response):
        books = response.xpath("//div[@class='h4']/a/@href").getall()
        yield from response.follow_all(books, self.parseBook)

        pagination_links = response.xpath("//ul[@class='pagination']/li/a/@href").get()
        yield from response.follow_all(pagination_links, self.parse) 
    
    def parseBook(self, response):
        for book in response.xpath("//div[@class='col-sm-7 book-detail']"):
            yield {
                'name': book.xpath("//div[@class='col-sm-7 book-detail']/div/h1/text()").get(),
                'art':  book.xpath("//div[@class='col-sm-7 book-detail']/div[3]/span/text()").get(),
                'series':  book.xpath("//div[@class='col-sm-7 book-detail']/div[4]/span/a/text()").get(),
                'lang':  book.xpath("//div[@class='col-sm-7 book-detail']/div[5]/span/a/text()").get(),
                'year':  book.xpath("//div[@class='col-sm-7 book-detail']/div[6]/text()").get(),
                'cover':  book.xpath("//div[@class='col-sm-7 book-detail']/div[7]/text()").get(),
                'page':  book.xpath("//div[@class='col-sm-7 book-detail']/div[8]/text()").get(),
                'format':  book.xpath("//div[@class='col-sm-7 book-detail']/div[9]/text()").get(),
                'ISBN':  book.xpath("//div[@class='col-sm-7 book-detail']/div[10]/text()").get(),
                'publisher':  book.xpath("//div[@class='col-sm-7 book-detail']/div[11]/span/a/text()").get(),
                'barcode':  book.xpath("//div[@class='col-sm-7 book-detail']/div[12]/text()").get(), 
                'price':  book.xpath("//div[@class='price_value']/text()").get(),
                'description':  book.xpath("//div[@class='book-description-column']/p[2]/font/text()").getall(),
            }
