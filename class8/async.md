# 线/进程池
python 3.2开始在标准库中新增了concurrent.futures模块,它主要提供了'ProcessPoolExecutor', 'ThreadPoolExecutor' 两个类,提供了线/进程池的支持

它们的使用方法相同:
```python
with ProcessPoolExecutor(max_workers) as pool:
    pool.submit(task, args) # 返回Future对象
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


```python
import socket
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


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
```
因为socket需要3次握手成功才能简历起连接,而3次握手的过程中,需要通过网络来传递信息,这需要的时间是不确定的,socket连接是会一直阻塞进程,直至3次握手成功,才继续执行下面的代码.
但是,如果对方服务器出现网络问题,而无法握手成功,那么socket就会一直阻塞,直至timeout,即使网络通畅,socket连接仍然需要不短时间
这时程序处理请求需要很长时间,假如处理1个请求要1秒,那么处理10个请求就需要10秒

```python
# 多进程
def multiproc_way():
    start = time.time()
    with ProcessPoolExecutor(10) as executor:
        proc_pool = {executor.submit(blocking_way, url) for url in urls}
    # use 0.6353843212127686
    result = [proc.result() for proc in proc_pool]
    print(time.time() - start)
    return proc_pool
```
多进程的使用使用,使得处理时间大幅度降低,利用多核CPU的资源,使得多个进程并行,从而加快程序处理速度, 但是这样做的代价就是需要消耗更多的资源.
下面来看多线程:
```python
# 多线程
def multithread_way():
    start = time.time()
    with ThreadPoolExecutor(10) as executor:
        thread_pool = {executor.submit(blocking_way, url) for url in urls}
    # use 0.5409300327301025
    result = [proc.result() for proc in thread_pool]
    print(time.time() - start)
```
多线程执行时,其实每个线程还是阻塞的,
python中,由于有GIL的存在,多个线程之间实际上是不能在同一个时间并行的
多个线程中,其实每个线程还是阻塞的,只不过每个线程执行指定的指令数或者指定的时间就会释放GIL锁,让其他线程继续执行
实际运行的只有获取到GIL锁的那个线程,而当线程中遇到需要等待的操作时,切换到其他线程中继续执行代码,无形中就会减少代码的运行时间

---
下面来看看非阻塞方式
```python
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
```
sock.setblocking(False) 把socket设置为非阻塞模式,那么socket 执行connect, recv等操作时是不会阻塞程序的
但是问题随之而来socket 执行完connect后再执行send操作,send的时候如何才能知道socket的连接已经成功建立了呢？
这时就需要不断循环去尝试,直至连接建立,并发送请求后,才继续执行下面的代码,而recv时也是同理.

这样看起来,程序更加复杂,而且效率也没有得到提升,因为socket虽然是非阻塞的,但是代码中在send,recv时还是需要等待上一步的操作完成时才能执行
那么如果有一个人可以在socket建立完成时来通知程序,可以执行send操作了,那样在等待socket建立的过程中,CPU就可以去干其他的事情了.
简单的例子:周末去吃饭,但是餐厅人很多,需要等位,这时候如果你一直在这里等,你就不能走开去干其他事情,直至吃完饭之后.
那么如果你把电话号码留给服务员,让他在轮到你的时候给你电话,让你过来吃饭,那么在等待电话到来之前,你可以去干你想干的事情.

- epoll:提供了专门的系统模块让应用程序可以接收事件通知(把电话号码留给服务员)
- callback:在知道I/O状态发生改变后所需要执行的操作(服务员打电话通知可以过去吃饭)
```python
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
        crawl = Crawler('url')
        crawl.fetch()
    loop()
    print(time.time() - start)
```
register(fileobj, events, data=None) 

selector.register 在该socket的写事件上绑定了回调函数connected.在该socket上第一次发生的写事件意味着连接的建立后会调用connected函数

而connected函数在连接建立成功后再解除了该socket上所有绑定的数据。

在connect函数中同样也用selector.register 绑定了read_response函数,当socket发生可读事件(即服务器已经返回数据)时调用read_response函数.

这些事件触发后,我们就要执行回调了,我们可以用selector.select()来获取所触发的事件,当没有事件被触发时selector.select()会阻塞,直至事件触发.


```python
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
        selector.register(conn, EVENT_READ, self.handle)

    def handle(self, key, mask):
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
```

原理与刚才一样,当Chat.run()时在该socket的写事件上绑定了回调函数accept函数.在该socket上第一次发生的读事件意味着有新客户端连接后会调用accept函数
执行accept时又会把socket绑定到handle函数上,当socket发生可读事件(即有数据可获取时),调用handle函数,获取clinet发过来的数据,并转发到其他的client
