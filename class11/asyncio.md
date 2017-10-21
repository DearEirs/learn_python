# async库的使用


### 事件循环策略
```
# 全局对象  每个进程1个
# 获取当前Python进程的事件循环策略
policy = asyncio.get_event_loop_policy()
# 设置当前Python进程的事件循环策略
policy = asyncio.set_event_loop_policy(policy)

# uvloop第三方库提供的事件循环策略
# 效率上会比asyncio默认的事件循环策略会高,但稳定性稍低

# 事件循环上下文 实际上指线程, 每个Python线程可以设置不同的事件循环
```

### loop
```
# 获取
loop = asyncio.get_event_loop()
# asyncio.get_event_loop() 等于 asyncio.get_event_loop_policy().get_event_loop()
# 一般情况下可以用get_event_loop 来获取时间循环, 但是在子线程中,必须使用后者
# 这是因为asyncio会为主线程设置默认的事件循环策略和事件循环,但子线程并没有

# 设置
loop = asyncio.set_event_loop(loop)
loop = asyncio.get_event_loop_policy().set_event_loop(loop)

# 创建
loop = asyncio.new_event_loop()
loop = asyncio.get_event_loop_policy().new_event_loop()

# 同一个进程中,最好只使用1个事件循环策略,在多线程的情况下,只使用该策略生产的事件循环对象
# 主线程  程序执行的入口

# 运行
loop.run_until_complete(future) # 运行loop 直至future set_result即协程执行完成或返回错误
loop.run_forever() # 一直运行loop, 直至loop被stop,如果在stop前 loop已经接受到了Task事件,那么loop会在所有已接受到的事件完成后才暂停
loop.is_running() # 返回bool 判断loop是否在运行
# 暂停
loop.stop() # 暂停loop 
# 停止
loop.close() # 直接关闭loop,当前执行中的任务,将要执行的回调都不会执行.这个操作无法回滚,慎用.
loop.is_close() # 返回bool 判断loop是否已经关闭
# 当loop关闭即close后,该loop就不能再使用,如果还想使用事件循环的话,需要重新创建一个

```

### Task
```python
# 显示创建Task的3种方式
1. task = asyncio.Task(coro, *, loop=None)
2. task = asyncio.ensure_future(coro, *, loop=None) 
3. task = loop.create_task(coro) # 调用Task类 只接受coro

# ensure_future
# 可以接收coro, future, future-like
# 接受到coro,传递给create_task
# 接受到future直接return
# 接收到future-like, 把future-like 包装到coro 再传递给create_task

```

### Future
```python
# 区分
concurrent.futures
为多线程多进程执行异步任务准备
asyncio.future
为单线程内协程做异步做准备

# 显示创建Future
asyncio.future(loop)
loop.create_future

future.set_result(retult) # 标记future完成并设置其结果
future.add_done_callback(func) # 添加回调, 当future被标记为完成时执行
```

### 其他
```
async def func():
  pass

# func --> 函数
# func() --> 返回一个协程

# 使用async def 定义协程时, 里面可以没有await
# 使用async def 定义协程时, 不能使用yield from

# 实现了__await__方法的对象也称为future-like对象

# awaitable 对象
# 1.调用原生协程对象的原生协程
# 2.被@asyncio.coroutine 装饰的生成器函数调用后返回的生成器协程
# 3.实现了__await__魔术方法的对象(__await__ 必须返回迭代器, 否则会报TypeError),实现了__await__的对象也被称为类似未来对象(Future-like)

# 异步数据库相关的第三方库
# motor --> mongodb
# aiomysql --> mysql
# aioredis --> redis
```

### 多个协程同时执行
```
1. asyncio.wait(fs, *, loop=None, timeout=None, return_when='ALL_COMPLETED')
return 2组Future 一组为已经完成(done)的,一组是还在等待完成(pedding)的
# 可通过await asyncio.wait(tasks)来获取协程的返回结果
# 该接口不会引发TimeoutError,当任务超时(timeout)时 返回pedding组的Future
# Note: This does not raise TimeoutError! Futures that aren't done,when the timeout occurs are returned in the second set.
# 接收多个future,可以通过return_when 来设置loop在什么时候返回
# ALL_COMPLETED,全部Future都执行完成得到结果时才return
# FIRST_COMPLETED, 任意Future执行完得到结果时return
# FIRST_EXCEPTION, 任意Future抛出异常时return,如果没有异常抛出,就直至所有Future执行完成才return

2. asyncio.as_completed(fs, *, loop=None, timeout=None)
# 返回一个按完成顺序生成协程的迭代器
# 每当协程执行完成,可以马上处理返回结果
# 但是有可能接受到除fs以外的协程
# 需要遍历返回的Iterator并await iter 才能获取返回结果

3. asyncio.gather(*coros_or_futures, loop=None, return_exceptions=False)
# 将协程组合成1个组同时执行,等到所有协程都执行完成时才会返回结果
# await asyncio.gather(*task) 返回的直接是tasks的结果列表,结果按原始顺序生成
# 如果return_exceptions为True,则任务中的异常被视为与成功结果相同,并在结果列表中收集;否则,第一个引发的异常将立即传播到返回的future
# 如果外部future被取消,那么给定的所有future都将取消
```
