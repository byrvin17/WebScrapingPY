from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import MapCompose
_autor_ = 'ByronLima'

class HabitacionItem(Item):
    tipo = Field()
    personas = Field()

class Airbnb(CrawlSpider):
    name = "Habitaciones"
    start_urls = ['https://www.airbnb.com/s/Loja']
    allowed_domains = ['airbnb.com']

    rules = (
        Rule(LinkExtractor(allow= r'page=')),
        Rule(LinkExtractor(allow= r'/rooms'), callback='parse_items')
    )

    def parse_items(self, response):
        item = ItemLoader(HabitacionItem(), response)
        item.add_xpath('tipo','//*[@id="summary"]/div[2]/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div/div/span/a[1]/text()')
        item.add_xpath('personas','//*[@id="summary"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/span/text()', MapCompose(lambda i: i[0]))
        yield item.load_item()