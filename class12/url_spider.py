#!/bin/env python
#!encode:utf-8

import asyncio
import aiohttp
import aiomysql
import aioredis

from lxml import etree

import settings
from models.redis_client import RedisClient


class URLCrawl:
    def __init__(self, loop):
        self.loop = loop

    async def inert_to_redis(self, urls):
        for url in urls:
            await self.r.sadd(pre_read_url, url)
        urls = ' '.join(urls)
        await self.r.sadd(all_urls, urls)
        url = await self.r.spop(pre_read_url)
        if url:
            asyncio.ensure_future(self.fetch())
        else:
            self.stop()

    async def get_url_from_redis(self):
        url = await self.r.spop(pre_read_url)
        return url

    async def fetch(self, url=None):
        if not url:
            url = await self.get_url_from_redis()
        async with aiohttp.Client(loop=loop) as session:
            async with session.get(url, headers=headers) as response:
                response = await response.read()
                await self.r.sadd(has_read, url)
                asyncio.ensure_future(get_url(response))
                return response

    async def get_url(self, response):
        html = etree.HTML(response)
        urls = set(html.xpath(xpath['//a/@href']))
        asyncio.ensure_future(insert_to_redis(urls))
        return urls

    async def run(self):
        self.r = await RedisClient(self.loop).connect()
        asyncio.ensure_future(self.fetch())

    def stop(self):
        self.loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    url_crawl = URLCrawl(loop)
    asyncio.ensure_future(url_crawl.run())
    loop.run_forever()
