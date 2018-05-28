# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from drugs.items import DrugsItem
from scrapy.http import Request


class Dr1Spider(scrapy.Spider):
    name = 'dr1'
    allowed_domains = ['drugs.dxy.cn']
    a = urllib.parse.quote(input("输入商品名称：").encode(encoding='utf-8',errors='strict'))
    b = urllib.parse.quote(input("输入厂商名称：").encode(encoding='utf-8',errors='strict'))
    url = "http://drugs.dxy.cn/search/drug.htm?keyword="
    start_urls =[url+a+"+"+b]

    print(start_urls)
    def parse(self, response):
        if response.xpath("//div[@class='common_hd clearfix']/div[1]/text()").extract()[0]=='药品搜索结果':
            print("no drug!")
            url1 =  response.xpath("//ul[@class='list']/li/div[1]/h3/a/@href").extract()[0]
            print(url1)
            yield Request(url1, callback=self.parse)


            return 0
        else:
            i = DrugsItem()
            i["dName"] = response.xpath("//div[@class='m49 detail detail1']/dl/dd[1]/text()").extract()
            i["dIngredients"] = response.xpath("//div[@class='m49 detail detail1']/dl/dd[2]/text()").extract()
            i["dIndications"] = response.xpath("//div[@class='m49 detail detail1']/dl/dd[3]/text()").extract()
            i["dDosage"] = response.xpath("//div[@class='m49 detail detail1']/dl/dd[5]/text()").extract()
            i["dAdverse_reactions"] = response.xpath("//div[@class='m49 detail detail1']/dl/dd[6]/text()").extract()
            i["dTaboo"] = response.xpath("//div[@class='m49 detail detail1']/dl/dd[8]").extract()
            i["dApproval_Number"] = response.xpath("//div[@class='m49 detail detail1']/dl/dd[13]/text()").extract()
            print(i["dName"])
            print(i["dIndications"])
            print(i["dIngredients"])
            print(i["dDosage"])
            print(i["dAdverse_reactions"])
            print(i["dTaboo"])
            aa
            return i
