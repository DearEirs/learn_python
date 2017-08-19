# 用代码来验证课程所讲内容

```
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
```

- 类(Class) ：Humen
- 对象（Object）：数据成员：xiaoming.name|age|hight|weight,方法：xiaoming.__init__|walk|sleep
- 实例（ Instance ）：xiaoming
- 类变量（Class variable）：count
- 实例变量（Instance variable）：xiaoming.name|age|hight|weight
- 数据成员（ Data member ）：xiaoming.name|age|hight|weight
- 方法（Method）：xiaoming.__init__|walk|sleep 和其他内置方法


```
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

实例化（ Instantiation ）：daming = Man('xiaoming', 28, 170, 120)
继承（ Inheritance ）：class Man(Humen):
函数重载（Function overloading）：
运算符重载（Operator overloading）：
派生类/子类:class Man
基类/父类:classHumen
```

```
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
```
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
