# 用代码来验证课程所讲内容

### 函数的意义
```python
#函数是对单一相关操作的有组织的可重用代码的块的封装
#为应用程序提供更好的模块化以及提高代码的复用程度
def func1(x, y, z):
    return x + y + z

def func2():
    x, y, z = 1, 2, 3
    return x + y + z 

func1(x=1,y=2,z=3)
func2()

# 函数并不意味着对一段重复使用的代码进行封装 如func2,在x, y, z,不变的情况下这样使用好像不会出问题
# 但是我们要的不仅仅是这个,在有可能的情况下,应该尽可能地提高函数的自定义程度,
如同func1，传到函数里边的可以是3个str,3个int,3个list等等,让使用者来自己定义函数的输入
```
### 定义和调用规则

- 定义函数
- 写漂亮的文档字串
- 返回值
- 调用函数
- 接收返回值
- 内置函数与自定义函数

```python
def send_mail(sender, password, receiver,  message, subject=None, smtpserver='qq.smtp.com') -> bool:
    ''' function send_mail
    
    :param sender: 发件人的邮箱地址
    :type sender: str
    
    :param password: 发件人的邮箱密码
    :type password: str
    
    :param receiver: 收件人的邮箱地址
    :type receiver: list
    
    :param message: 邮件内容
    :type message: str
    
    :param subject: 邮件标题
    :type subject: str
    
    :param smtpserver: 邮件服务器, 默认为'qq.smtp.com'
    :type smtpserver: str
    
    :return bool
    '''
    msg=MIMEText(message)
    msg['Subject']=subject
    msg['Form']=sender
    msg['To']=receiver
    result = False
    try:
      smtp=SMTP()
      smtp.connect(smtpserver)
      smtp.login(sender,password)
      smtp.sendmail(sender,receiver,msg.as_string())
      smtp.close()
      retult = True
    except Exception as e:
      print(e)
      result = False
    return result

result = send_mail('369574757@qq.com', '123456', ['369574757@qq.com'], 'Hello World')
print(result)

# 定义函数  从def所在行开始 直至函数所在的最后1行
# 函数注释： 函数里边第一个注释块 help()会返回函数的注释
# 函数返回值： return 所返回的值(默认为None)
# 调用函数: send_mail() | result = send_mail()
# 接收返回值： result = send_mail()
# 内置函数与自定义函数：
# send_mail()就是自定义函数
# 内置函数-->不需要用户自己定义就能调用的(list,dict,tuple等)
```


### 函数的传参方式 按绑定关系传递

```python

str1 = "dear"
list1 = []

print(sys.getrefcount(list1)) -> 2

def func(s:str, l:list):

  print(sys.getrefcount(list1)) -> 5
  print(sys.getrefcount(l)) -> 5
  print(id(l),l)

  l.append(s)
  print(id(l),l)
  
  s += "Eirs"
  print(id(s),s)

# 由sys.getrefcount(list1)统计得知在参数传递的过程中  只是把list1的绑定关系传递给l 相当于l = list1 
# 由于l.append(s)只是对[]进行修改,并没有改变l与[]的绑定关系  所以两次print出来的id 是一样的
# s += "Eirs" 把变量s重新指向了新的元素'dearEirs', 变量从绑定'dear' 变为绑定'dearEirs'所以值的内存地址变了
```

### 传参的形式


```python
def func(a, b, c=6, *args):
  return id(a),id(b),id(c)
  
def func(x, y, z):
  return x-y+z


func(1, 2, 3) #在第一、二、三位的参数1,2,3分别对应着参数x,y,z 所以叫按位置传参
```

- 必选参数: a, b   func(1, 2)
- 可选参数（默认参数): c  func(1, 2) func(1, 2, 3)
- 按位置传参: func(1,2,3)  在第一、二、三位的参数1,2,3分别对应着参数a, b, c
- 关键字参数: func(a=1, b=2, c=3)
- 可变长参数: func(1,2,3,4,'dear'),在a,b,c 都接收到参数后,其余参数传递给*args

### 匿名函数

```python
lambda x: x % 2

相当于
def func(x):
  return x % 2

#使用情景: 函数体可以用1条表达式就可以解决时
```



### 作用域

```python
#!/usr/bin/env python

x = 1

if True:
  y = 2

for i in range(5):
  z = x+i

def func(x,y,z):
  total = x + y + z
  print(total)
  return total

#print(total)
total = func()
print(total)

```

- 全局作用域：在当前py文件里都生效
- 局部作用域：从函数或类的定义开始到该函数或类最后1行代码 为该函数或类的 局部作用域
- 全局变量：定格定义的变量（包含定格的if while for try里边定义的变量），在全局生效,可用globals()查看
- 局部变量：在函数或类里边所定义的变量，只在该函数或类中生效,可用locals()查看

### 生命周期
```python

a = 10000
sys.getrefcount(a) -> 2
del a
sys.getrefcount(a) -> 1
#变量a的生命周期结束,如果不del a   那么变量a将会一直存在 直至程序关闭

#函数的生命周期
def func(x,y,z):
  total = x + y + z
  print(total)
  return total
  
#从函数第一行开始 到函数 return 返回值 若没return则到函数代码里的最后1行执行结束  即为函数的生命周期

#对象的生命周期
当对象被垃圾回收机制回收时,对象才会结束它的生命周期
```

# 垃圾回收
### 引用计数

```python
# sys.getrefcount() 统计变量所指向内存地址被引用的次数
a = 1000
sys.getrefcount(a) -> 2

b = c  = a 
sys.getrefcount(a) -> 4
sys.getrefcount(b) -> 4
sys.getrefcount(c) -> 4

# 每当有1个变量1000时  1000的引用计数就会加1  a, b, c, d,都指向着1000

del a 

sys.getrefcount(a) -> 1
sys.getrefcount(b) -> 3
sys.getrefcount(c) -> 3

当变量a被销毁时, 1000的引用次数就会减1
```

### 分代收集

```python
# gc.get_count() 查看当前回收计数
# gc.get_threshold() 查看回收阈值 -> (700, 10, 10)

```

# 闭包
- 前提1：嵌套函数
- 前提2：内层函数引用非全局变量
- 前提3：不改变外部变量的绑定关系
查看函数是不是闭包：
2.7:func.func_closure  返回cell对象即为闭包  返回None即不是
3.6:func.__closure__

```python
def outer():
  dict1 = {}
  def inner(key,value):
    dict1[key] = value
    return dict1
  return inner

f1 = outer()
print(f.__closure__) -> (<cell at 0x000002BEE0BC57C8: dict object at 0x000002BEE0FD5F78>,)
f1('key1','value1')
f1('key2','value2') -> {'key1': 'value1', 'key2': 'value2'}

f2 = outer()
f2('key3','value3')
f2('key4','value4') -> {'key3': 'value3', 'key4': 'value4'}

# 当外部函数被调用时，返回一个闭包 即f,f2
# 闭包 = 子函数 + 依赖的外部变量  子函数 inner 外部变量 dict1
# 闭包是一种特殊的函数
# 每调一次外部函数，返回一个新闭包 f f2 的互不干扰,是2个不一样的闭包 各自指向着不同的内存地址


# 匿名函数可不可以是闭包

def outer():
  dict1 = {}
  l = lambda key, value: dict1.update({key:value})
  return l

f = outer()
print(f.__closure__) -> (<cell at 0x00000230A4645798: dict object at 0x00000230A46E2168>,)

```
 
