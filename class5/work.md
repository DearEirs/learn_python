# 用代码来验证课程所讲内容

面向对象的基本特点
- 封装
- 继承
- 多态
---
### 基本概念
```python
class Humen:
  count = 0
  def __init__(self, name, age, hight, weight)
    self.name = name
    self.age = age
    self.hight = hight
    self.weight = weight
    count += 1
  
  def walk(self):
    print("walk slow")
  
  def sleep(self):
    pass

xiaoming = Humen('xiaoming', 18, 180, 100)
'''
类(Class) ：用户通过定义一组属性以定义一种对象的原型，用于表征该类的任何对象。属性是指数据成员（类变量和实例变量）和方法。
对象（Object）：根据类定义的实例，包含数据成员与方法。
实例（ Instance ）：类的一个单独的对象，是该类所代表的原型的特定实例之一。
类变量（Class variable）：被类的所有实例共享的变量。类变量定义在类里，但再任何方法之外。
实例变量（Instance variable）：定义在方法内部，且只属于当前实例的变量。
数据成员（ Data member ）：类或实例的变量，用于保存相关联的数据。
方法（Method）：定义在类里面的函数，代表着类的实例具有的行为。
'''
```

- 类(Class) ：Humen
- 对象（Object）：数据成员：xiaoming.name|age|hight|weight,方法：xiaoming.__init__|walk|sleep
- 实例（ Instance ）：xiaoming
- 类变量（Class variable）：count
- 实例变量（Instance variable）：xiaoming.name|age|hight|weight
- 数据成员（ Data member ）：xiaoming.name|age|hight|weight
- 方法（Method）：xiaoming.__init__|walk|sleep 和其他内置方法

### 基本概念
```python
# 承接上面

class Man(Humen):
  def __init__(self):
    super().__init__()
  
  def __add__(self, value):
    self.age = self.age + value
    return self.age
  
  def walk(sefl):
    print('walk fast')

daming = Man('xiaoming', 28, 170, 120)
daming + 1
print(daming.age) -> 29

实例化（ Instantiation ）：daming = Man('daming', 28, 170, 120)
继承（ Inheritance ）：class Man(Humen):
函数重载（Function overloading）：
运算符重载（Operator overloading）：
派生类/子类:class Man
基类/父类:classHumen
```

```python
class A:
  def __new__(cls, *args, *kwargs):
    print("method __new__ run")
    
  def __init__(self):
    print("method __init__ run")
  
  def func(a):
    pass

a = A()
# 输出
# "method __new__ run"
# "method __init__ run"
# 类在实例化过程中, 会先执行__new__ 再执行__init__
# __new__ 方法的第一个参数为cls  __init__ 方法的第一个参数为self
# 可以理解为 实例化类时 需要把类cls传到 __new__方法去构造1个实例  得到self 然后__init__再对实例self进行初始化
# 但是在类中定义方法时.可以把self 换成其他字符串, 这样是可以行 但是不建议这么做,
# 因为使用self和cls 是开发者们的一个"约定",而且使用self,cls更容易让人理解

```

### 属性访问
```python
class B:
  def __init__(self, name):
    self.name = name

b = B('Dear')
b.name  -> 'Dear'
getattr(Object, name, defalut)
getattr(b, 'name') -> 'Dear'
b.__getattribute__('name') -> 'Dear'
getattr(b, 'age') -> AttributeError
getattr(b, 'age', 18) -> 18
hasattr(obj, name)
hasattr(b, 'name')  -> True
hasattr(b, 'haha')  -> False
setattr(Object, name, value)
setattr(b, 'name', 'haha')
b.name -> 'haha'
setattr(b, 'age', 18) == b.__setattr__('age', 18) == b.age=18
b.age -> 18
delattr(obj, name)
delattr(b, 'age') == b.__delattr('age')
```

### 内置属性
```python
class C:
  ''' This is Object C '''
  def __init__(self, name, age):
    pass

c = C('Dear', 18)
print(c.__dict__)  -> {'name': 'Dear', 'age': 18} #当前实例所拥有属性组成的字典
# c.a = 1  == c.__dict__[a] = 1 
print(c.__doc__)  -> 'This is Object C' #与函数注释一样会被help函数显示
print(c.__module__)  -> '__main__' #显示函数被那个模块所调用,当前为__main__
print(C.__bases__) -> (<class 'object'>,) #由父类组成的元组, 注意用的是类C 而不是实例c 
#类在没有继承其他类的情况下,默认会继承object类
```

### 继承与多继承
```python
class Father:
  def __init__(self, first_name, name)
    self.first_name = name
  
  def full_name():
    return first_name + name
  
  def func(self):
    print("Fater's func")

class Child(Father):
  def __init__(self, gender, name):
    self.gender = gender
    self.name = name
  
  def func(self):
    print("Child's func")
  
  def father_func(self):
    super().func()

class Child2(Child, Father): #多继承时,如继承的类之间有继承关系,那么子类需写在父类前面
  pass

f = Father('chen', 'ergou')
c = Child('Male', 'sangou')
c.first_name -> 'chen' #子类可以继承父类的数据成员与方法
c.func() -> 'Child's func' #也可以重写父类的数据成员与方法
c.father_func() -> "Fater's func" #子类可以通过super() 来调用父类中的方法
c2 = Child2() 
issubclass(Child2, Father) -> True #判断Child2 是否为 Father 的子类
isinstance(Father, Child2) -> True #判断Father 是否有 Chile2 的子类

```

### 常内置方法重载
```python
class D:
  def __init__(self, host, port):
    self.host = host
    self.port = port
    print('connect db')
    
  def __del__(self)
    print('disconncet db')
    
  def __repr__(self):
    return '__repr__'
    
  def __str__(self):
    return '__str__'
  
  def __len__(self):
    return  1

d = D('192.168.0.1', '3306') -> 'connect db'  #__init__ 方法在类实例化时就会调用
print(d) -> '__str__' #__str__方法在打印实例信息时被输出,必须返回str
repr(d) -> '__repr__' #打印实例信息时,若__str__里没返回信息 那么就会把__repr__的信息返回,同样__repr__返回的必须是str
# 当__str__和__repr__ 都没返回信息时  默认打印类的信息 如<__main__.F object at 0x000001C904692A58>
len(d) -> 1 #__len__ 方法在len(Object) 时被调用
```

### 常用运算符重载
```python
class E:
  flag = True
  def __init__(self, value):
    self.value = value
  
  def __bool__(self):
    return Flag
  
  def __add__(self, value):
    self.value = self.value + value
    return self.value
  
  def __radd__(self, value):
    return self.value
  
  def __iadd__(self, value):
    self.value += value
    return self.value
  
  def __or__(self, value):
    reslut = self.value or value
    return reslut
  
  def __lt__(self, value):
    reslut = self.value < value
    return reslut
  
  def __gt__(self, value):
    reslut = self.value > value
    return reslut
  
  def __le__(self, value):
    result = self.value <= value
    return result
  
  def __ge__(self, value):
    result = self.value >= value
    return result

'''
__bool__（self）: 使用bool(object) 时触发
__add__(self, other): 使用object + other 时触发
__radd__(self, other): 使用other + object 时触发
__iadd__(self, other): 使用object += other 时触发
__or__(self, other): 使用object or other 时触发
__lt__(self, other): 使用object <  other 时触发
__gt__(self, other): 使用object >  other 时触发
__le__(self, other): 使用object <= other 时触发
__ge__(self, other): 使用object >= other 时触发
lt = less than
gt = greater than
le = less and equal
ge = greater and equal
'''
```

### 属性隐藏
```python
class F:
  def __init__(self):
    self._name = 'Dear'
    self.__age = 18

f = F()
f._name in dir(f) -> True
f.__age in dir(f) -> False
# python 实际在不存在只能由该类访问的私有属性 只是通过一些方法隐藏起来
# _name 保护性质的属性,不建议修改, 可以通过f._name 来访问得到
# __age 私有性质的属性,但是实际上还是可以访问得到,通过 __ 所定义的"私有属性" 在python中会被转成 _Object__Attr 即_F__age
# _F__age 通过命名方式就可以大概知道 __age 这个属性是属性 F 这个类的
```

### 类方法与静态方法
```python

def encrypt(password):
  return md5(password)

class Login:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.login(username, password)
  
  @classmethod
  def login_by_phone(cls, phone):
    print('connect db')
    print('get username and password by phone')
    return cls(username,password)
  
  @staticmethod
  def encrypt(password):
    return md5(password)
  
  def login(self, username, password):
    #password = encrypt(password) #效果一样
    password = self.encrypt(password)
    print(login)

cls == class Object
self == 实例本身

login = Login.login_by_phone(13123456789)
'''
@classmethod：常用于定义备选构造方法，
@staticmethod：静态方法和在普通的非class的method作用是一样的，只不过是命名空间是在类里面。
一般使用场景就是和类相关的操作，但是又不会依赖和改变类、实例的状态。
'''
```

# 设计程序
```python
# Hosts 主机类
# Salt_Hosts 被Salt 监控的主机类
# Salt_Master Salt Master 类, 管理minion包括Syndic的minion
# Salt_Syndic Syndic类 管理自己的minion 但被master 管理

class Hosts:
  def __init__(self, hostname, ip)
    self.hostname = hostname
    self.ip = ip

  def is_alive(self):
    pass
  
  


class Salt_Hosts(Hosts):
  def __init__(self, hostname, ip, salt_id)
    super().__init__(hostname, ip)
  
  def salt_run(self):
    #在本机执行salt命令 所有salt客户端都可执行
    pass

  def is_master(self):
    #判断机器是否为master 
    pass

  def is_syndic(self):
    #判断机器是否为Syndic
    pass


class Salt_Master(Salt_Hosts):

  def keys_manager(self, target=None, action='list-all' ):
    # 秘钥管理 根据action 与target 作出相关操作
    pass

  def excute_cmd(self, target, cmd):
    # 对指定target 执行命令  salt target cmd.run cmd 
    # 常用
    pass
  
  def excute_sls(self, target, sls):
    # 对指定target 执行命令 salt target state.sls sls
    pass

  def excute_salt_cmd(self, target, cmd):
    #  执行自定义的salt 命令
    #  target = '*'
    #  cmd = 'pillar.get os'
    #  salt '*' pillar.get os
    pass

  def install_minions(self, target):
    # 使用salt-ssh 对target 安装salt-minion客户端
    pass

def Salt_Syndic(Salt_Master):

  def __init__(self, hostname, ip, salt_id, master)
    self.salt_id = salt_id
    self.master = master
    super().__init__(hostname, ip)
```
