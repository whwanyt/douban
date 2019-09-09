# -*- coding: utf-8 -*-
import scrapy
from Douban.items import DoubanItem

class DoubamovieSpider(scrapy.Spider):
    name = 'doubamovie'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = "https://movie.douban.com/top250?start="
    start_urls = [
        url+str(offset),
    ]
    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath("//div[@class='info']")
        print "-----"
        for each in movies:
            item['title'] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]
            bd = each.xpath(".//div[@class='bd']/p/text()").extract()[0]
            item['star'] = each.xpath(".//span[@class='rating_num']/text()").extract()[0]
            quote = each.xpath(".//p[@class='quote']/span/text()").extract()
            item['bd'] = "".join(bd).strip()
            if len('quote') != 0:
                item['quote'] = quote[0]

            yield item
            print "----"
        if self.offset <225:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)


        # //div[@class="info"]//span[@class="title"][1]/text()
        # 电影信息
        # //div[@class="info"]//div[@class="bd"]/p/text()
        # 评分
        # //div[@class="info"]//span[@class="rating_num"]/text()
        # 简介
        # //div[@class="info"]//p[@class="quote"]/span/text()


