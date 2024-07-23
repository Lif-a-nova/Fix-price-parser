import scrapy

from fix_price.items import Product


class PriceSpider(scrapy.Spider):
    """Неисполняемый паук - ItemSpider"""
    name = "price"
    allowed_domains = ["fix-price.com"]
    start_urls = ["https://fix-price.com/catalog/kosmetika-i-gigiena/p-3120074-zubnaya-schetka-olgate-11-sht-v-assortimente"]

    def parse(self, response):
        """
        Код для работы.
        пока не разобралась
        """
        # не извлекает
        # возможно нужно выполнить JS
        original_price = response.css(
             'div.price-quantity-block div.regular-price.old-price::text'
             ).get()
        original_price = float(original_price.replace('₽', '').replace(' ', '').strip())

        # не извлекает
        current_price = response.css(
             'div.price-quantity-block div.special-price::text'
             ).get()
        if current_price is None:
             current_price = original_price
        else:
            current_price = float(current_price.replace('₽', '').replace(' ', '').strip())

        discount_percentage = 0
        if original_price != current_price:
            discount_percentage = ((original_price - current_price) / original_price) * 100 

        sale_tag = None
        if discount_percentage != 0:
            sale_tag = f'Скидка {discount_percentage}%'

        price = {
            'current': current_price,
            'original': original_price,
            'sale_tag': sale_tag,
        }

        item = Product()
        item['price'] = price
        yield item



