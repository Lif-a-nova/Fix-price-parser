from datetime import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
from fix_price.items import Product
from fix_price.settings import (CATEGORIES, DOMAIN)


class CategorySpider(CrawlSpider):
    """Исполняемый паук - CategorySpider"""
    name = "category"
    allowed_domains = [DOMAIN]
    start_urls = CATEGORIES

#    for url in start_urls:
    rules = (
        Rule(LinkExtractor(restrict_css='div.controls a')),
        Rule(LinkExtractor(restrict_css='div.description a'), callback="parse_item", follow=True),
        )


    def parse_item(self, response):
        """Вывод результатов, которые прогружаются"""
        url =  response.url,
        address = str(url).split('p-')
        rpc = address[1][0:7]
        title = response.css('h1::text').get()
        brand = response.css('div.properties span.value a::text').get()
        section = response.css('a.link.nuxt-link-active span::text').getall()

        main_img = response.css('img.normal::attr(src)').get()
        set_img = (
            response.css('div.product-images img::attr(src)').getall()
        )

        assets = {
            'main_image': main_img,
            'set_images': set_img,
            # на сайте не представлены
            'view360': None,
            'video': None,
        }

        description = response.css('div.product-details div.description ::text').get()
        metadata = {
            '__description': description,
        }
        meta_inf = response.css('div.properties p.property')

        for inf in meta_inf:
            title = inf.css('span.title *::text').get()
            value = inf.css('span.value *::text').get()
            metadata.update({title : value})

        item_var = response.css('img.thumbs-image::attr(src)').getall()
        variants = len(item_var) if item_var else 1

        item = Product()
        item['timestamp'] = int(datetime.timestamp(datetime.now()))
        item['RPC'] = rpc
        item['url'] = url
        item['title'] = title
        item['brand'] = brand
        item['section'] = section
        item['assets'] = assets
        item['metadata'] = metadata
        item['variants'] = variants
        yield item
