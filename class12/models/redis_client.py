#!/bin/env python
#!encode:utf-8

import asyncio
import aioredis
import settings


class RedisClient:
    def __init__(self, loop):
        self.host = settings.REDIS_HOST
        self.port = settings.REDIS_PORT

    async def connect(self):
        self.conn = await aioredis.create_connection((self.host, self.port))
        return self.conn

    async def close(self):
        await self.conn.close()
