装饰器作用:在不改变原代码的情况下增强原代码的功能

装饰器返回的是可调用的(函数)对象,可调用的(函数)对象,可调用的(函数)对象。

##### 不要被@迷惑
@只是一个语法糖
```python
1.
def func1(func):
    print(1)
    
@func1
def func2():
  pass

func2()

2.
def func1(func):
    print(1)

def func2():
    pass

func1(func2)

'''
第一段代码中的func2()和第二段代码中的func1(func2)是等价的
@只是一个语法糖,当使用
@func1
def func2()
  pass

func2 会被重新定义成func1(func2)
相当于
a = 1000
a = a + 1
这是a已经不再是1000了 而是通过a+1得出来的结果1001  而1000早已经被销毁
'''
```

---

装饰器的使用:

情景1:实现用户访问某些网页时,需要先登录,如果没登录就重定向到登录界面
```python
def login_required(func):
    login_url = 'login.html'
    if 'user is not login':
        print('please login first')
        return redirect(login_url)
    def wrapper(*args, *kwargs):
        result = func()
        return result
    return wrapper

@login_required
def func():
    pass
```
这时每次调用func时 就会先判断用户是否已经登录,然后再执行func函数里边对应的操作

情景2:但是有时候login_url 并不是固定的  所以我们需要在使用时自定义返回的页面
```python
def login_required(login_url='login.html')
    if not isinstance(login_url,str):
        login_url = 'login.html'
    def wrapper(func):
        login_url = 'login.html'
        if 'user is not login':
            print('please login first')
            return redirect(login_url)
        def _wrapper(*args, *kwargs):
            result = func(*args, *kwargs)
            return result
        return _wrapper
    return warpper

@login_required(login_url='login2.html')
def func():
    pass
```
这时候,只需要在最外边再定义一层函数来接收调用装饰器时所传递的参数就可以

这时候的func = login_required(login_url='login2.html')(func)(*args, *kwargs)

##### 同时使用多个装饰器:
```
def outer1(func):
    def inner1():
        print('inner1 first')
        func()
        print('inner1 second')
    return inner1

def outer2(func):
    def inner2():
        print('inner2 first')
        func()
        print('inner2 second')
    return inner2

def outer3(func):
    def inner3():
        print('inner3 first')
        func()
        print('inner3 second')
    return inner3

@outer1
@outer2
@outer3
def func():
    print('Hello World')

```
当出现同时多个装饰器时,装饰器会从下往上执行

1. @outer3  func() = outer3(func)  --> 返回inner1
2. @outer2  outer2(func) = outer2(outer3(func)) --> outer3(func)== func 被传入outer2
3. @outer1  outer1(func) = outer1(outer2(outer3(func))) --> outer2(outer3(func)) == func 被传入outer1

所以实际执行顺序为

1. outer1(func):  --> print('inner1 first')
2. outer1(func):  --> func() == outer2(outer3(func))
3. outer2(func):  --> print('inner2 first')
4. outer2(func):  --> func() == outer3(func)
5. outer3(func):  --> print('inner3 first')
6. outer3(func):  --> func() == func() (装饰器外定义的)
7. func():        --> print('Hello World')
8. outer3(func):  --> print('inner3 second')
9. outer2(func):  --> print('inner2 second')
10. outer1(func): --> print('inner1 second')

##### 用类来做装饰器

##### 实现@X 
@X func = X(func)   --> init

@X func() = X(func)()  --> init call

```python
class DecoClass:
    def __init__(self, func):
        self.func = func
    def __call__(self):
        print('执行func前')
        result = self.func()
        print('执行func后')
        return result

@DecoClass
def func():
    print('Hello World')
```

##### 实现@DecoClass(args)
```python
class DecoClass:
    def __init__(self, args):
        self.arg = args
    def __call__(self, func):
        def inner(*args, **kwargs):
            print(self.arg)
            print('执行func前')
            result = func(*args, **kwargs)
            print('执行func后')
            return result
        return inner

@DecoClass(1)
def func(*args, **kwargs):
    print('Hello World')
```
#@DecoClass(1) 其实是被__init__接收的 而func则被__call__接收
#@DecoClass(1) func = DecoClass(1)(func)   DecoClass(1)初始化 返回的是实例   实例() 则调用__call__


##### 实现@DecoClass.deco
```python
class DecoClass:
    #[@classmethod|@staticmethod]
    def deco(func):
        def inner(*args, **kwargs):
            print('执行func前')
            result = func(*args, **kwargs)
            print('执行func后')
            return result
        return inner

@DecoClass.deco
def func():
    print('Hello World')
```

##### 实现@DecoClass.deco(1)
```python
class DecoClass:
    def deco(arg):
        def outer(func):
            def inner(*args, **kwargs):
                print(arg)
                print('执行func前')
                result = func()
                print('执行func后')
                return result
            return inner
        return deco

@DecoClass.deco(1)
def func():
    print('Hello World')
```

##### 实现@decoclass
```
class DecoClass:
    def __call__(self, func):
        def inner(*args, **kwargs):
            print('执行func前')
            result = func(*args, **kwargs)
            print('执行func后')
            return result
        return inner

decoclass = DecoClass()
@decoclass
def func():
    print('Hello World')
```

##### 实现@decoclass(args)
```python
class DecoClass:
    def __call__(self, *args, **kwargs):
        def outer(func):
            print(args)
            def inner(*args, **kwargs):
                print('执行func前')
                result = func(*args, **kwargs)
                print('执行func后')
                return result
            return inner
        return outer

decoclass = DecoClass()
@decoclass(1)
def func():
    print('Hello World')
```

##### 实现@decoclass.deco
```python
class DecoClass:
    def deco(self, func):
        def inner(*args, **kwargs):
            print('执行func前')
            result = func(*args, **kwargs)
            print('执行func后')
            return result
        return inner


decoclass = DecoClass()
@decoclass.deco
def func():
    print('Hello World')
```

##### 实现@decoclass.deco(args)
```python
class DecoClass:
    def deco(self, *args, **kwargs):
        def outer(func):
            print(args)
            def inner(*args, **kwargs):
                print('执行func前')
                result = func(*args, **kwargs)
                print('执行func后')
                return result
            return inner
        return outer


decoclass = DecoClass()
@decoclass.deco(1)
def func():
    print('Hello World')
```
