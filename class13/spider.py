#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-11-11 14:43:25


import asyncio
import time
import urllib.parse


from components import RedisMixin, HtmlMixin, SavePictureMixin
from settings import REDIS_CONFIG
from settings import MYSQL_CONFIG



class BaseSpider(RedisMixin, HtmlMixin, SavePictureMixin):
    def __init__(self, domain, loop):
        self.domain = domain
        self.loop = loop
        self.stoped = False

    async def url_schedule(self):
        r_pool = await self.create_redis_pool(REDIS_CONFIG)
        urls = await self.get_url(self.domain)
        if not urls:
            print('please put a url in redis')
            time.sleep(5)
        for url in urls[:3]:
            asyncio.ensure_future(self.url_spider(url))
        asyncio.ensure_future(self.url_schedule())

    async def url_spider(self, url):
        response = await self.get_response(url)
        urls = None
        try:
            urls = response.xpath('//a/@href')
        except AttributeError as e:
            print(response,'error')
        urls = filter(lambda url: self.domain in url, urls)
        urls = map(lambda url: url.strip('/').strip(), urls)
        asyncio.ensure_future(self.get_data(response, url))
        for url in urls:
            await self.save_url(self.domain, url)

    async def get_data(self, response, url):
        pass

    def run(self):
        asyncio.ensure_future(self.url_schedule())

    def stop(self):
        self.stoped = True
        self.loop.stop()


class PocoSpider(BaseSpider):
    async def get_data(self, response, url):
        data = response.xpath('//*[@id="content"]')
        await self.read_url(self.domain, url)
        if data:
            pictures = data[0].xpath('//img/@src')
            for picture in map(lambda x:str(x), pictures):
                if not isinstance(url, str):
                    url = url.decode('utf-8')
                if self.domain not in picture:
                    picture = url.split('/')[2] + '/' + picture.strip('/')
                if not await self.has_picture(self.domain, picture):
                    await self.save_picture(picture)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    spider1 = PocoSpider('poco.cn', loop)
    spider.run()
    loop.run_forever()
