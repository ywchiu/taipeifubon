# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
class TutorialPipeline(object):
    def open_spider(self, spider):
        CREATE_SQL = '''
            CREATE TABLE IF NOT EXISTS money(
               title   VARCHAR(500),
               content TEXT,
               category VARCHAR(50),
               url VARCHAR(500),
               dt DATETIME
            );
        '''
        self.conn = sqlite3.connect('news.sqlite')
        self.cur = self.conn.cursor()
        self.cur.execute(CREATE_SQL)

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        col = ','.join(item.keys())
        placeholders = ','.join(len(item) * '?')
        sql = 'insert into money({}) values({});'
        self.cur.execute(sql.format(col, placeholders), tuple(item.values()))
        return item

