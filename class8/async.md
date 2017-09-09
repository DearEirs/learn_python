# 线/进程池
python 3.2开始在标准库中新增了concurrent.futures模块,它主要提供了'ProcessPoolExecutor', 'ThreadPoolExecutor' 两个类,提供了线/进程池的支持

它们的使用方法相同:
```python
with ProcessPoolExecutor(max_workers) as pool:
    pool.submit(task, args)
    pool.running() # 判断task是否在运行
    pool.done() # 判断task是否执行完成
    pool.result() # 获取task的返回值
    pool.map(task, iterable) # 迭代iterable,并当作参数传到task执行(有序)
```

1. pool.submit 会返回Future对象
2. Future:可以简单理解为是未来将会完成的操作
3. 异步编程就是把需要等待的操作变成future,而释放CPU去执行其它代码


# 初涉异步
# 基本概念
- 阻塞:程序在等待某个操作完成期间，自身无法继续干别的事情，则称该程序在该操作上是阻塞的。
- 非阻塞:程序在等待某操作过程中，自身不被阻塞，可以继续运行干别的事情，则称该程序在该操作上是非阻塞的。
- 同步:不同程序单元为了完成某个任务，在执行过程中需靠某种通信方式以协调一致，称这些程序单元是同步执行的。
- 异常:为完成某个任务，不同程序单元之间过程中无需通信协调，也能完成任务的方式。



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


import socket
from selectors import DefaultSelector, EVENT_READ

selector = DefaultSelector()


class Chat:
    def __init__(self, host, port, max_clients):
        self.clients = []
        self.host = host
        self.port = port
        self.stoped = False
        self.max_clients = max_clients

    def run(self):
        self.sock = socket.socket()
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.max_clients)
        self.sock.setblocking(False)
        selector.register(self.sock, EVENT_READ, self.accept)
        self.loop()

    def accept(self, key, mask):
        print('accept')
        conn, addr = self.sock.accept()
        self.clients.append(addr)
        conn.setblocking(False)
        selector.register(conn, EVENT_READ, self.send)

    def send(self, key, mask):
        selector.unregister(key.fd)
        print('send')
        conn = key.fileobj
        print(conn.getpeername())
        try:
            data = conn.recv(4096)
        except BlockingIOError:
            pass
        if data:
            for client in self.clients:
                if client != conn.getpeername():
                    self.sock.sendto(data, client)

    def loop(self):
        while not self.stoped:
            events = selector.select()
            for event_key, event_mask in events:
                callback = event_key.data
                callback(event_key, event_mask)

    def stop(self):
        self.stoped = True


if __name__ == '__main__':
    chat = Chat('localhost', 8000, 10)
    chat.run()
