#!/bin/env python
#!encode:utf-8

from lxml import etree
import asyncio
import aiohttp
import aiomysql
import aioredis

from models.redis_client import RedisClient
from models.mysql_client import MysqlClient

class Pipeline:
    def __init__(self, data):
        self.data = data
        self.data_filter()

    def data_filter(self):
        # 修改或筛选数据
        return self.data

class DataCrawl:
    def __init__(self, loop):
        self.loop = loop

    async def get_url_from_redis(self):
        url = self.r.spop()
        return url

    async def fetch(self, url=None):
        if not url:
            url = await get_url_from_redis()
        async with aiohttp.Client(loop=loop) as session:
            async with session.get(url, headers=headers) as response:
                response = await response.read()
                await self.r.sadd(has_read, url)
                asyncio.ensure_future(get_data(response))
                return response

    async def get_data(self, response):
        html = lxml.HTML(response)
        data = html.xpath('@text()')
        data = Pipeline(data)
        await asyncio.ensure(insert_into_mysql(data))
        return data

    async def insert_into_mysql(self, data):
        self.m.insert(table, data)
        url = await get_url_from_redis()
        if url:
            asyncio.ensure_future(url=url)
        else:
            self.stop()

    async def run(self):
        self.r = await RedisClient(self.loop).connect()
        self.m = await MysqlClient(self.loop).connect()
        asyncio.ensure_future(self.fetch())

    async def stop(self):
        self.loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    data_crawl = DataCrawl(loop)
    asyncio.ensure_future(data_crawl.fetch())
    loop.run_forever()
