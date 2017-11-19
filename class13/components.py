#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-11-12 14:51:28

import aiomysql
import aioredis
import aiohttp
import os

from lxml import etree


class CountMixin:
    pass


class DataSpiderMixin:
    def save(self, conn, data):
        pass


class SavePictureMixin:
    async def save_picture(self, url, *, path='/data/pictures'):
        async with aiohttp.ClientSession(loop=self.loop) as session:
            async with session.get(url) as response:
                data = await response.read()
        filename = url.split('/')[-1]
        full_path = os.path.join(path, filename)
        with open(full_path, 'wb+') as f:
            f.write(data)
            print('save picture:%s' % full_path)


class HtmlMixin:
    async def get_response(self, url):
        url = url.decode('utf-8')
        async with aiohttp.ClientSession(loop=self.loop) as session:
            async with session.get(url) as response:
                response = await response.read()
                response = etree.HTML(response)
                return response


class RedisMixin:
    async def create_redis_pool(self, config):
        host = config.get('host', '127.0.0.1')
        port = config.get('port', 6379)
        self.pool = await aioredis.create_pool((host, port), loop=self.loop)
        return self.pool

    async def save_url(self, domain, url):
        if 'javascript' in url:
            url = url.split('\'')[1]
            print(url,'---------------------------')
        with await self.pool as p:
            await p.sadd(domain, url)

    async def read_url(self, domain, url):
        with await self.pool as p:
            # print('read_url:%s' % url)
            await p.sadd(domain + '_had_read', url)

    async def get_url(self, domain):
        with await self.pool as p:
            urls = await p.sdiff(domain, domain + '_had_read')
            return urls

    async def has_picture(self, domain, url):
        with await self.pool as p:
            urls = await p.sismember(domain + '_pictures', url)
            return urls

class MysqlMixin:
    async def get_mysql_conn(self, config):
        self.host = config.get('host', '127.0.0.1')
        self.port = config.get('port', 3306)
        self.db = config.get('db', None)
        self.user = config.get('user', 'root')
        self.password = config.get('password', None)
        self.conn = await aiomysql.connect(self.host, self.port, self.user, self.passwd,
                                           self.db, self.loop)
        return self.conn

    async def insert_data(self, data, *, table='spider_data'):
        async with self.conn.cursor() as cursor:
            result = await cursor.execute(sql)
