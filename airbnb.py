from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import MapCompose
_autor_ = 'ByronLimaRojas'

class HospedajeItem(Item):
    camas = Field()
    banios = Field()
    dormitorios = Field()
    huespedes = Field()
    tipo = Field()

class Airbnb(CrawlSpider):
    name = "Hospedaje"
    start_urls = ['https://www.airbnb.com/s/Loja']
    allowed_domains = ['airbnb.com']

    rules = (
        Rule(LinkExtractor(allow=r'page=')),
        Rule(LinkExtractor(allow=r'/rooms'), callback='parse_items')
    )

    def parse_items(self, response):
        item = ItemLoader(HospedajeItem(), response)
        item.add_xpath('camas',
                       '//*[@id="summary"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/span/text()',
                       MapCompose(lambda i: i[0])),
        item.add_xpath('banios',
                       '//*[@id="summary"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/span/text()',
                       MapCompose(lambda j: j[0])),
        item.add_xpath('dormitorios',
                       '//*[@id="summary"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/span/text()',
                       MapCompose(lambda k: k[0])),
        item.add_xpath('huespedes',
                       '//*[@id="summary"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/span/text()',
                       MapCompose(lambda l: l[0])),
        item.add_xpath('tipo',
                       '//*[@id="summary"]/div[2]/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div/div/span/a[1]/text()')
        yield item.load_item()