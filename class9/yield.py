#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-09-14 10:01:35

import os
import time
from concurrent.futures import ThreadPoolExecutor


pool = ThreadPoolExecutor(5)

files = ['file1', 'file2', 'file3', 'file4']


def blocking_func(file):
    '''
    阻塞
    '''
    new_file = os.open('new1', os.O_WRONLY | os.O_NONBLOCK)
    new_file = os.fdopen(new_file, 'a')
    with open(file) as f:
        data = f.read()
        new_file.writelines(data)
        new_file.close()


def futures_gen():
    ···
    生成器,启用线程池执行文件读写操作,并返回Future对象
    ···
    for file in files:
        future = pool.submit(blocking_func, file)
        yield future


def coro_way():
    futures = []
    for future in futures_gen():
        futures.append(future)
    # return [future.result() for future in futures]
    # 这里的return会阻塞进程 等待文件完成写入


if __name__ == '__main__':
    start = time.time()
    coro_way()
    print(time.time() - start)

    start = time.time()
    with open('new2', 'a') as nf:
        for file in files:
            with open(file) as f:
                data = f.read()
                nf.writelines(data)
    print(time.time() - start)

 
'''
1. 调用coro_way函数
2. 访问生成器
3. 生成器开启线程执行文件读写操作
4. 程序返回coro_way函数 继续执行代码
'''
