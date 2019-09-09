# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import time

import pymysql
from scrapy.conf import settings
class DoubanPipeline(object):
    def __init__(self):
        # 用户名：root 密码：root 数据库名：douban
        self.db = pymysql.connect(host='localhost', db='douban', user='root', passwd='root', charset='utf8')
        self.cursor = self.db.cursor()
        print '------'

        self.cursor.execute('Drop table if EXISTS doub')  # 如果表存在就删除
        sql = """CREATE TABLE doub (
                            `id` int(10) NOT NULL AUTO_INCREMENT,
                           `title` char(20) NOT NULL,
                           `bd` char(100) DEFAULT NULL,
                           `star` char(20) DEFAULT NULL,
                           `quote` char(100) DEFAULT NULL,
                           PRIMARY KEY (`id`)
                         );"""
        self.cursor.execute(sql)
    def process_item(self, item, spider,):

        print '---kaishixieru-'
        list = dict(item)
        print list

        print '---xieru---'
        sql = 'insert into doub(title,bd,star,quote) VALUES ('+'\''+list['title']+'\''+','+'\''+list['bd']+'\''+','+'\''+list['star']+'\''+','+'\''+list['quote']+'\''+')'

        self.cursor.execute(sql)
        print '---xieru---'
        print '------'

    def close_spider(self, spider):

        self.db.commit()
        self.cursor.close()
        self.db.close()
