# 代码的基本优化,调试

### 构造与初始化方法
- __init__() 不是构造方法，它负责控制对象变量的初始化
- __new__() 才是构造方法，它负责控制对象的创建

```python
class A:
  def __new__(cls):
    print('正在创建类')
  
  def __init__(cls):
    print('类已经被创建')
    print('正在初始化类变量')

a = A()
```

### 对象序列化
- json：最常见，效率稍差，但跨平台、跨语言、结构好
- pickle：比json效率稍微高一点点，只支持Python
- cPickle：效率比上述两者都高很多
- protobuf：Google提供的第三方库，效率更高，跨平台，跨语言，结构紧凑体积小，内存节省和传输效率更好，
但需引入第三方库，提前设计好的数据结构不可随意改动

在序列化还没成为程序的瓶颈时,一般来说使用json就可以满足大部分需求.

序列化：是把对象转换成可以write到文件里边的数字、字符、字符串
```python
dict1 = {'key%i' % i:'value%i' % i for i in range(100000)}
f = open(r'C:\Users\Dear\Desktop\test.txt','ab')

json.dump(d,f) #直接写入文件
j = json.dumps(dict1) #把dict1 转换成json格式
d = json.loads(j) # 把j反序列化为dict格式


pickle.dump(dict1,f) #直接写入文件
p = pickle.dumps(d)  #输出序列化后的二进制字符串
d = pickle.loads(p) # 把p反序列化为dict格式


f.close()
```

### 配置文件解析
```python

'''
configparser INI风格
文本形式类似 key value
'''

[db]
db_host = 127.0.0.1
db_port = 22
db_user = root
db_pass = rootroot

[concurrent]
thread = 10
processor = 20
'''

conf = configparser.ConfigParser()
conf.read(r'C:\Users\Dear\Desktop\default.conf')
conf.sections() --> ['db', 'concurrent']
conf.options('db') --> ['db_host', 'db_port', 'db_user', 'db_pass']
```

### 多个分支条件

- if...elif...elif...
- 借助字典消除这种风格
- 实在消除不掉注意先后顺序安排(在可读性差不多的情况下,尽量把匹配率高的条件写在前面)

```python
# 需求需要多重判断,实现类似与其他语言中switch case的效果

ansers_dict = {
          'a' : 1,
          'b' : 2,
          'c' : 3,
          'd' : 4,
}

question = ('人有多少个鼻子?')
print(ansers_dict)
while True:
  anser = read('请选择 a,b,c,d中的一个')
  if anser in ansers_dict:
    print('你选择的是%s,人有%s个鼻子', % (anser,ansers_dict[anser]))
    break
```

### 短路运算
- and：前一个表达式为假不再进行后一个表达式的计算
- or：前一个表达式为真不再进行后一个表达式的计算

```python
# and
timeit.timeit('if 0 and 1 : pass',number=100000000) --> 1.397503963655573
timeit.timeit('if 1 and 0 : pass',number=100000000) --> 2.149041756294938

# or
timeit.timeit('if 1 or 0 : pass',number=100000000)  --> 1.587524198216385
timeit.timeit('if 0 or 1 : pass',number=100000000)  --> 2.823067097259937

```

### 成员测试

判断一个元素是否在某个容器（列表、集合、字典、字符串序列）时，直接用 in 或 not in 操作符判断，无需用 find 、 index 等方法

```python
timeit.timeit('list1 = [i for i in range(1000,1010)];list1.index(1005)',number=10000000) --> 11.784954835659846
timeit.timeit('list1 = [i for i in range(1000,1010)];1005 in list1 ',number=10000000) --> 9.56750599126508
```

### 内置排序

- sort(): 只是 list 的一个方法，直接修改原列表，返回值为None
- sorted(): 可排序所有可迭代对象，返回排序后的结果

```python
list1 = [3,41,2,5,1]

new_list = sorted(list1)
print(list1) --> [3,41,2,5,1]
print(new_list) --> [1,2,3,5,41]

list1.sort()
print(list1) --> [1,2,3,5,41]
```

### list、tuple、set选择
- list：有序、可变长、元素可重复
- tuple：有序、不可变长、元素可重复
- set：无序、可变长、元素不可重复

决绝万年list,决绝万年list,决绝万年list,
一般来说:
长度,元素不可变的情况下 选tuple
对顺序无要求,元素不可重复的情况下,选set
其他情况下才考虑list

### 避免命名空间污染

尽量使用 import a.B 的形式，而不是使用 from a import B

```python
from a import B
import a.b

class b:
  pass



b(1) --> Error
a.b(1) --> Sucess
```

### True & False
python2.x 中 if True 会比 if 1 慢
python3.x 中 没有这个问题

python2.x 中 True相当于一个指向1的变量,使用True时 需要先把内存中的1提取出来再做判断
#python2.x
```
>>> def func():
...   if 1:
...     pass
...
>>> def func2():
...   if True:
...     pass
...
>>> dis.dis(func)
  3           0 LOAD_CONST               0 (None)
              3 RETURN_VALUE
>>> dis.dis(func2)
  2           0 LOAD_GLOBAL              0 (True)   
              3 POP_JUMP_IF_FALSE        9

  3           6 JUMP_FORWARD             0 (to 9)
        >>    9 LOAD_CONST               0 (None)
             12 RETURN_VALUE
```
#python3.x
```
>>> import dis
>>> def func():
...   if 1:
...     pass
...
>>> def func2():
...   if True:
...     pass
...
>>> dis.dis(func)
  3           0 LOAD_CONST               0 (None)
              2 RETURN_VALUE
>>> dis.dis(func2)
  3           0 LOAD_CONST               0 (None)
              2 RETURN_VALUE
```

### 变量值交换
推荐使用 x, y = y, x
性能更快且可读性高

### 上下文管理器
尽量使用 with...as... 来实现对象的上下文管理，避免忘记显式地关闭资源
with 结束时 系统会自动关闭打开的对象
```
# 写一个可用于上下文管理的对象

```

### 字符串连接
- join 与 + 两种方式
- 前者更省内存

```python
list1 = ['a' for i in range(100000)]

def func():
  s = ''.join(list1)
  
def func2:
  s = ''
  for i in list1:
    s += i

timeit.timeit(func,number=10000) --> 4.525133861871087
timeit.timeit(func2number=10000) --> 

```

### 深浅拷贝

- 浅拷贝 copy.copy(obj) 只拷贝“第一层”对象
- 深拷贝 copy.deepcopy(obj) 递归拷贝“每一层”对象
- 不论深浅拷贝，不会为 全由不可变对象组成的对象 申请新内存空间
对象 with as
