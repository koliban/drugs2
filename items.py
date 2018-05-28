# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DrugsItem(scrapy.Item):
    # define the fields for your item here like:
    content=scrapy.Field()
    link=scrapy.Field()
    dName=scrapy.Field()
    dIngredients=scrapy.Field()
    dIndications=scrapy.Field()
    dDosage=scrapy.Field()
    dAdverse_reactions=scrapy.Field()
    dTaboo=scrapy.Field()
    dApproval_Number=scrapy.Field()
    check=scrapy.Field()
