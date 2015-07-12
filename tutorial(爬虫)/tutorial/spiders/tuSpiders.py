# -*- coding: utf-8 -*-
##import scrapy
##
##from tutorial.items import TutorialItem
##
##class DmozSpider(scrapy.Spider):
##    name = "dmoz"
##    allowed_domains = ["dmoz.org"]
##    start_urls = [
##        "http://www.dmoz.org/Computers/Programming/Languages/Python/",
##    ]
##
##    def parse(self, response):
##        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
##            url = response.urljoin(href.extract())
##            yield scrapy.Request(url, callback=self.parse_dir_contents)
##
##    def parse_dir_contents(self, response):
##        for sel in response.xpath('//ul/li'):
##            item = TutorialItem()
##            item['title'] = sel.xpath('a/text()').extract()
##            item['link'] = sel.xpath('a/@href').extract()
##            item['desc'] = sel.xpath('text()').extract()
##            yield item

import time as tm
import datetime as dt
import re

import scrapy
from tutorial.items import TutorialItem

def GetDtTime(tmstr):
    producetime = dt.datetime.strptime(tmstr, '%Y/%m')
    return producetime
    
def GetDistance(distr):
    ptstr = r'^(\d*)(.)(\d*)([\D\d]*)'
    DisPattn = re.compile(ptstr)
    disInfo = DisPattn.search(distr).groups()
    #tmpstr = disInfo[0] + disInfo[1] + disInfo[2]
    Distnce = int(disInfo[0])*10000+ int(disInfo[2])*100      
    return Distnce

def GetPrice(Pricestr):
    ptstr = r'^([^\d]*)(\d*)(.)(\d*)([\D\d]*)'
##    print Pricestr
    PricePattn = re.compile(ptstr)
    PriceInfo = PricePattn.search(Pricestr).groups()
##    for item in PriceInfo : print item
    Price = int(PriceInfo[1])*10000+ int(PriceInfo[3])*100      
    return Price


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
##        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
##        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        "http://www.xin.com/quanguo/s/o2a10i1v1l01/",
        "http://www.xin.com/quanguo/s/o2a10i1v1l02/",
        "http://www.xin.com/quanguo/s/o2a10i1v1l03/",
        "http://www.xin.com/quanguo/s/o2a10i1v1l04/",
        "http://www.xin.com/quanguo/s/o2a10i1v1l05/",
        "http://www.xin.com/quanguo/s/o2a10i1v1l06/",
        "http://www.xin.com/quanguo/s/o2a10i1v1l07/",
        "http://www.xin.com/quanguo/s/o2a10i1v1l08/",
        "http://www.xin.com/quanguo/s/o2a10i1v1l09/",
        "http://www.xin.com/quanguo/s/o2a10i1v1l10/",
        "http://www.xin.com/quanguo/s/o2a10i1v1l11/",
        "http://www.xin.com/quanguo/s/o2a10i1v1l12/",
        "http://www.xin.com/quanguo/s/o2a10i1v1l13/",
        "http://www.xin.com/quanguo/s/o2a10i1v1l14/",
        "http://www.xin.com/quanguo/s/o2a10i1v1l15/"
    ]




    def parse(self,response):
##        for sel in response.xpath('//ul/li'):
##            item=CheItem()
##            item['title']=sel.xpath('a//div[@class="vtc-info"]/title/text()').extract()
##            item['time']=sel.xpath('a//div[@class="box"]/ul/li[1]/text()').extract()
##            item['distance']=sel.xpath('a//div[@class="box"]/ul/li[2]/text()').extract()
##            item['gearbox']=sel.xpath('a//div[@class="box"]/ul/li[3]/text()').extract()
##            item['city']=sel.xpath('a//div[@class="box"]/ul/li[4]/text()').extract()
##            item['price']=sel.xpath('a//div[@class="vtc-money"]/em/text()').extract()
##            item['level']=sel.xpath('a//li/a[@class="car-class"]/text()').extract()
        #获得车型level
        i=0
        while i < len(self.start_urls):
            if self.start_urls[i] == response.url: break
            i = i + 1
        level = i + 1
        
        for sel in response.xpath('//div[@class="car-vtc vtc-border "]'):
            item=TutorialItem()
            item['title']=sel.xpath('div[@class="vtc-info"]/p/a/text()').extract()[0]
            strlist = sel.xpath('div[@class="vtc-info"]/div[@class="box"]/ul/li/text()').extract()
            item['time'] = GetDtTime(strlist[0])
            item['distance']=GetDistance(strlist[1])
            item['gearbox']=strlist[2]
            item['city']=strlist[3]
            item['price']=GetPrice(sel.xpath('div[@class="vtc-money"]/em/text()').extract()[0])
            item['level']=level

##            item['time'] = strlist[0]
##            item['distance']=strlist[1]
##            item['gearbox']=strlist[2]
##            item['city']=strlist[3]
##            item['price']=sel.xpath('div[@class="vtc-money"]/em/text()').extract()[0]
##            item['level']=level            
##            tmplist = []
##            tmplist.append(level)
##            item['level']= tmplist
            #sel.xpath('a//li/a[@class="car-class"]/text()').extract()
            yield item
##        filename = response.url.split("/")[-2] + '.txt'
##        with open(filename, 'wb') as f:
##            kkk = response.xpath('//div[@class="car-box clearfix"]/text()').extract()[0]
##            f.write(kkk)
