import asyncio
import aiomysql

import settings


class RedisClient:
    def __init__(self, loop):
        self.host = settings.MYSQL_HOST
        self.port = settings.MYSQL_PORT
        self.db = settings.MYSQL_DB
        self.user = settings.MYSQL_USER
        self.passwd = settings.MYSQL_PASSWD
        self.loop = loop

    async def connect(self):
        self.conn = await aiomysql.connect(self.host, self.port, self.user, self.passwd,
                                                     self.db, self.loop)
        return self.conn

    async def insert(self, table, data):
        # insert data into table
        pass

    async def close(self):
        await self.conn.close()
        return True
