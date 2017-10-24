# -*- coding: utf-8 -*-
import scrapy
import json
import re
from scrapy import Request
from ..db_helper import DBHelp

class JdSpider(scrapy.Spider):
    name = 'JD'
    allowed_domains = ['ai.jd.com']
    base_url = "https://ai.jd.com/index_new?app=Seckill&action=pcMiaoShaAreaList&callback=pcMiaoShaAreaList"
    start_urls = [base_url]
    db = DBHelp("miaosha")

    def parse(self, response):
        datas = json.loads(re.findall("pcMiaoShaAreaList\((.*)\)",response.text)[0],encoding="utf-8")
        # 获取没场的id
        groups = datas.get("groups")
        for group in groups:
            gid = group.get("gid")
            if gid == datas.get("gid"):
                continue
            yield Request(
                url=self.base_url + "&gid=%s"%group.get("gid"),
                callback=self.parse_other,
            )
        # 当前秒杀的列表
        miaoShaList = datas.get("miaoShaList")
        self.db.insert_many(miaoShaList)

    def parse_other(self,response):
        datas = json.loads(re.findall("pcMiaoShaAreaList\((.*)\)", response.text)[0], encoding="utf-8")
        # 即将要秒杀的商品
        miaoShaList = datas.get("miaoShaList")
        self.db.insert_many(miaoShaList)