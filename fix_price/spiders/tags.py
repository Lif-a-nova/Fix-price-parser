import scrapy

from fix_price.items import Product


class TagsSpider(scrapy.Spider):
    """Неисполняемый паук - TagsSpider"""
    name = "tags"
    allowed_domains = ["fix-price.com"]
    start_urls = ["https://fix-price.com/catalog/kosmetika-i-gigiena/p-3120074-zubnaya-schetka-olgate-11-sht-v-assortimente"]


    def parse(self, response):
        """
        Код для работы.
        пока не разобралась
        """
        # не извлекает
        marketing_tags = response.css('div.product-images div.wrapper.sticker *::text').getall()

        # не извлекает
        # сайт проверяет остатки по городам в отдельном окне
        # возможно, нужно перейти по ссылке и проверить на True "в наличии"
        in_stock = response.css('div.check-availability-block svg::attr(xmlns)').get()
        count = 0

        stock = {
            'in_stock': in_stock,
            'count': count
        }

        item = Product()
        item['marketing_tags'] = marketing_tags
        item['stock'] = stock
        yield item
