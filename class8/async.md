#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-09-07 21:18:25


import socket
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import pymysql


urls = [
    'https://www.duanwenxue.com/article/4642780.html',
    'https://www.duanwenxue.com/article/4642781.html',
    'https://www.duanwenxue.com/article/4642782.html',
    'https://www.duanwenxue.com/article/4642783.html',
    'https://www.duanwenxue.com/article/4642784.html',
    'https://www.duanwenxue.com/article/4642785.html',
    'https://www.duanwenxue.com/article/4642786.html',
    'https://www.duanwenxue.com/article/4642787.html',
    'https://www.duanwenxue.com/article/4642788.html',
]

domain = 'duanwenxue.com'

# 同步阻塞
def blocking_way(url):
    sock = socket.socket()
    sock.connect((domain, 80))
    request = 'GET {0} HTTP/1.0\r\nHost: {1}\r\n\r\n'.format(url, domain)
    sock.send(request.encode('ascii'))
    response = b''
    block = sock.recv(4096)
    while block:
        response += block
        block = sock.recv(4096)
    return response

def asyn_way():
    start = time.time()
    response = []
    for url in urls:
        response.append(blocking_way(url))
    # use 1.8566324710845947
    print(time.time() - start)
    return response

# 多进程
def multiproc_way():
    start = time.time()
    with ProcessPoolExecutor(10) as executor:
        proc_pool = {executor.submit(blocking_way, url) for url in urls}
    # use 0.6353843212127686
    _ = len([proc.result() for proc in proc_pool])
    print(time.time() - start)
    return proc_pool


# 多线程
def multithread_way():
    start = time.time()
    with ThreadPoolExecutor(10) as executor:
        thread_pool = {executor.submit(blocking_way, url) for url in urls}
    # use 0.5409300327301025
    _ = len([proc.result() for proc in thread_pool])
    print(time.time() - start)


# 非阻塞方式
def nonbroking_way():
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(("www.duanwenxue.com", 80))
    except BlockingIOError:
        pass
    request = 'GET {0} HTTP/1.0\r\nHost: {1}\r\n\r\n'.format(url, domain)
    data = request.encode('ascii')
    While True:
        try:
            sock.send(data)
            break
        except OSError:
            pass

    response = b''
    while True:
        try:
            chunk = sock.recv(4096)
            while chunk:
                response += chunk
                chunk = sock.recv(4096)
            break
        except OSError:
            pass
        return response

import socket
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector = DefaultSelector()
stopped = False
urls_todo = ['/', '/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9']

class Crawler:
    def __init__(self, url):
        self.url = url
        self.sock = None
        self.response = b''

    def fetch(self):
        self.sock = socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect(('www.baidu.com', 80))
        except BlockingIOError:
            pass
        selector.register(self.sock.fileno(), EVENT_WRITE, self.connected)

    def connected(self, key, mask):
        selector.unregister(key.fd)
        get = 'GET {0} HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'.format(self.url)
        self.sock.send(get.encode('ascii'))
        selector.register(key.fd, EVENT_READ, self.read_response)

    def read_response(self, key, mask):
        global stopped
        chunk = self.sock.recv(4096)
        if chunk:
            self.response += chunk
        else:
            selector.unregister(key.fd)
            urls_todo.remove(self.url)
            if not urls_todo:
                stopped = True

def loop():
    while not stopped:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback(event_key, event_mask)

if __name__ == '__main__':
    import time
    start = time.time()
    for url in urls_todo:
        craw = Crawler('url')
        craw.fetch()
    loop()
    print(time.time() - start)


class AsyncDB:
    def __init__(self, host, db, user, password, port=3306):
        self.host = host
        self.db = db
        self.user = user
        self.password = password

    def connect(self):
        self.conn = pymysql.Connect(host=host, db=db, user=user, password=password)
        return self.conn

    def insert()
