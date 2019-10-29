# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JogosItem(scrapy.Item):
    campeonato = scrapy.Field()
    diahorario = scrapy.Field()
    timecasa = scrapy.Field()
    timecasaabbr = scrapy.Field()
    timecasaimg_url = scrapy.Field()
    timevisitante = scrapy.Field()
    timevisitanteabbr = scrapy.Field()
    timevisitanteimg_url = scrapy.Field()
    placar_timecasa = scrapy.Field()
    placar_timevisitante = scrapy.Field()

