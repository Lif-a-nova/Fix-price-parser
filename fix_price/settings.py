
DOMAIN = "fix-price.com"
URL_MAIN = "https://fix-price.com/catalog"

# пока не разобралась, как передать выбор города,
# который не прописан в url
# LOCATION = 'Екатеринбург'

CATEGORIES = [
    f'{URL_MAIN}/kosmetika-i-gigiena/ukhod-za-polostyu-rta',
    f'{URL_MAIN}/dlya-doma/dlya-vannoy',
    f'{URL_MAIN}/kantstovary/kantselyarskie-prinadlezhnosti',
    ]

BOT_NAME = "fix_price"

SPIDER_MODULES = ["fix_price.spiders"]
NEWSPIDER_MODULE = "fix_price.spiders"

ROBOTSTXT_OBEY = False

# можно убрать в файл .txt
ROTATING_PROXY_LIST = [
    '95.174.127.48:3128',
]

DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}


CONCURRENT_REQUESTS = 16
DOWNLOAD_DELAY = 0.4

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'ru',
  'User-Agent': 'Mozilla/5.0(Windows NT 6.1; WOW64)'
}


REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

FEED_EXPORT_FIELDS = [
    'timestamp',
    'RPC',
    'url',
    'title',
    'brand',
    'marketing_tags',
    'brand',
    'section',
    'price_data',
    'stock',
    'assets',
    'metadata',
    'variants',
    ]
