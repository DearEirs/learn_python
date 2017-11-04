#!encode:utf-8
import os
import sys

# Redis config
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_PASSWD = None
REDIS_ENCODING = 'utf-8'

# Mysql config
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
MYSQL_DB = 'spider'
MYSQL_USER = 'dear'
MYSQL_PASSWD = 'spider'

# Start url
START_URL = ''

# headers
HEADERS = {}

# append import path
sys.path.append(os.getcwd())

