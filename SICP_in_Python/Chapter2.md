## 第二章

一个类表示一类对象, 
一个单独的对象称为类的一个实例
类可以通过像调用带有描述实例的参数的函数一样来创建实例

```python
from datetime import date # date与类绑定


today = date(2018, 1, 16)
```

date与类绑定, 代表着一类日期, 而date(2018, 1, 16)这个实例代表着2018年1月16日这一天, 参数就是对这个实例的描述


在python里边, 我们使用符号'.'来指定对象的属性
```python
<expression> . <name>
```

< expression > 的求值是一个对象, 而name是对象属性的名字
对象也有方法, 方法从对象的参数和对象本身计算出结果, 如:
```python
>>> today.strftime('%A, %B %d')
'Tuesday, February 16'
```
today这个对象接收了1个参数, 这个参数告诉他以何种格式展现日期, 但是我们并没有告知它显示哪个具体的日期,  它是从自己本身那里获取得.


在python里边所有的对象都有一个类型, type函数可以让我们检查一个对象的类型.
```python
>>> type(today)
<class 'datetime.date'>
```

原始数据类型:
  -  有一些原始的表达式可以对这些类型的对象求值，叫做标量
  - 有一些内建的函数、运算符和方法可以操作这些对象

实际上Python包含了三个原始数字类型: 整数(int),实数(float)和复数(complex).

数据抽象是一种方法,使我们能够隔离如何使用一个复合数据对象的细节,它是如何构建的.


一个元组的元素可以通过两种方式打开.

第一种方法是通过我们熟悉的多个赋值的方法.
```python
>>> pair = (1, 2)
>>> pair
(1, 2)
>>> x, y = pair
>>> x
1
>>> y
2
```

第二种访问元祖元素方法是通过索引操作符写成方括号的形式
```python
>>> pair[0]
1
```

python 中的元祖是由0索引开始的, 这意味着索引0选出第一个元素,索引1选出第二个元素,依此类推.这个索引约定的一个直觉就是索引代表了一个元素从元组开始偏移的距离.

元组是原生类型,这意味着Python内置的操作符可以操作它们.

一般来说,数据抽象的基本思想是为每种类型的值确定一组基本的操作,根据这些操作来表达对该类型值的所有操作,然后在操作数据时仅使用这些操作.

一般来说,我们可以想象一些由选择器和构造器集合定义的抽象数据类型，以及一些行为条件. 只要符合行为条件（如上面的分割属性）,这些函数构成数据类型的有效表示.


序列：
- 长度：序列拥有有限的长度
- 元素选择： 序列中的每个元素都有一个相对应的非负, 小于序列长度的下标, 它从0开始对应着序列的第一个元素.

框和指针表示法：
> 每个值 (复合或基元) 都被描述为指向框的指针.

![image](https://raw.githubusercontent.com/wizardforcel/sicp-py-zh/master/img/nested_pairs.png)

使一个元祖成为另外一个元祖的元素的能力, 为我们的编程语言提供了一种新的组合方法. 我们称元祖的这种嵌套能力为元素的封闭属性, 通常, 如果组合的结果本身可以使用相同的方法进行组合, 则合并数据值的方法将满足封闭属性, 封闭是任何组合方法的关键, 因为它允许我们创建层次结构——结构组成部分,它本身是由部分,等等, 结构的组成部分由结构本身组成. 



递归列表:
> 递归列表列表由一系列的值对表示, 每个值对的第一个元素是列表里边的元素, 第二个元素表示列表的剩余部分, 最后一个值对的第二个元素为None, 这表明列表已经结束


![image](https://raw.githubusercontent.com/wizardforcel/sicp-py-zh/master/img/sequence.png)

```python
>>> (1, (2, (3, (4, None))))
```

一个非空的序列可以分解为:
- 它的第一个元素
- 序列剩余的部分

```python
# 递归列表的实现
>>> empty_rlist = None # 定义空列表


>>> def make_rlist(first, rest): # 生成列表
        """Make a recursive list from its first element and the rest."""
        return (first, rest)
        
        
>>> def first(s): # 获取列表的第一个元素
        """Return the first element of a recursive list s."""
        return s[0]
        
  
>>> def rest(s): # 获取列表的第二个元素, 即剩余部分
        """Return the rest of the elements of a recursive list s."""
        return s[1]


# 这个时候我们就可以利用上边定义的方法来访问列表了

>>> counts = make_rlist(1, make_rlist(2, make_rlist(3, make_rlist(4, empty_rlist))))#相当于(1, (2, (3, (4, None))))
>>> first(counts) # 第一个元素是1
1
>>> rest(counts) # 第二个元素是列表的剩余部分
(2, (3, (4, None)))

# 递归列表可以存放一系列的值,但它还没有实现序列的抽象.使用抽象数据类型的定义,我们可以实现描述序列的两个行为:长度和元素的选择.

>>> def len_rlist(s): # 获取列表的长度
        """Return the length of recursive list s."""
        length = 0
        while s != empty_rlist:
            s, length = rest(s), length + 1
        return length
        
>>> def getitem_rlist(s, i): # 获取列表的指定元素
        """Return the element at index i of recursive list s."""
        while i > 0:
            s, i = rest(s), i - 1
        return first(s)
        
        
>>> len_rlist(counts)
4
>>> getitem_rlist(counts, 1)  # The second item has index 1
2

# 这时我们就已经实现了列表的2个基本功能, 计算长度, 元素选择
```

Mapping(映射)： 一个强大的方法, 把元组中每个元素当做参数传递到函数里边执行, 并收集调用函数返回的结果. **python3返回的是map类型, 可以通过tuple或list来强制类型转换**

map(func, *iterables) --> map object

for语句的组成：
```python
for <name> in <expression>:
    <suite>
```
for语句执行的过程：
1. 执行头部语句中的 <expression>, 它必须返回一个可迭代的值
2. 对于序列里的每一个值, 按顺序执行--把 <name> 绑定到局部栈帧, 然后执行子句
  
这个求值过程的一个重要结果是，在for语句执行完毕之后，name会被绑定到序列的最后一个元素上

序列解包: 程序中的一个常见模式是有一系列的元素, 它们本身是序列, 但都是固定的长度, For 语句可以在其header中包含多个name, 以便将每个元素序列 "解压" 到各自的元素中.

```python
>>> pairs = ((1, 2), (2, 2), (2, 3), (4, 4))
>>> for x, y in pairs:
        print(x, y)
# 当for循环执行时, x, y 会被依次与pairs的元素的第一/二个元素绑定
```

range是Python的另一种内建序列类型，它表示一个整数范围。由range函数来创建，它接受两个整数参数：所得范围是第一个数字到最后一个数字之间的范围(不包含1个数字).
range的使用方式:
```python
# range(stop) -> range object
# range(start, stop[, step]) -> range object
# start, stop, step 这3个参数都必须是整形, 其中step是可选参数, 默认为1
# start参数表示范围的起始值, stop表示范围的末尾, step表示步幅, 指从起始值到末尾值每次循环所取值的间隔

>>> tuple(range(1, 10)) # 包含1, 但不包含10
(1, 2, 3, 4, 5, 6, 7, 8, 9)
```

Slicing(切片): 在 Python 中, 序列切片与元素选择相似, 用方括号表示。冒号分隔起始和结束索引, 被省略的任何绑定都假定为极端值: 0表示起始索引,序列的长度表示结束索引

```python
>>> digits = [1, 2, 3, 4]
>>> digits[0:2]
[1,2]
>>> digits[1:] # 忽略了结束值, 所以假定结束值为极限值, 即序列的长度
[2,3,4]
```

字符串可以表达任意文本, 被单引号或者双引号包围, 字符串也是序列, 拥有序列的基本行为, 计算长度, 元素选择.

传统接口是一种数据格式, 它在多个模块化组件之间共享, 可以混合并匹配以执行数据处理。

需求: 对前 n 个斐波那契数列的偶数成员求和

具体步骤：
```python
 enumerate     map    filter  accumulate
-----------    ---    ------  ----------
naturals(n)    fib    iseven     sum

# fib 函数用于计算斐波那契数列
>>> def fib(k):
        """Compute the kth Fibonacci number."""
        prev, curr = 1, 0  # curr is the first Fibonacci number.
        for _ in range(k - 1):
             prev, curr = curr, prev + curr
        return curr


# iseven 函数判断数值是否是偶数
>>> def iseven(n):
        return n % 2 == 0
      
# filter 函数接收一个函数与一个序列, 依次把序列中的元素当作参数传到函数里边执行, 并返回序列的元素中判断为 true的元素


>>> def sum_even_fibs(n):
        """Sum the first n even Fibonacci numbers."""
        return sum(filter(iseven, map(fib, range(1, n+1))))
# map(fib, range(1, n+1) 计算出斐波那契数列
# filter(iseven, 斐波那契数列) 计算出数列中为偶数的值
# sum(偶数值的列表) 求和
```

通过引入nonlocal语句,我们已经创建了一个赋值语句的双重角色。它可以改变局部绑定,也可以改变非局部绑定。事实上,赋值语句已经有了一个双重角色:它们要么创建新的绑定或重新现有的名字.

正确分析non-local 语句代码的关键是要记住：
- 只有函数调用才能引入新的帧
- 赋值语句只会改变已经存在的栈帧的绑定关系.

可以使用列表构造函数复制列表。对一个列表的更改不会影响其他表, 除非它们共享结构。

```python
>>> suits = ['heart', 'diamond', 'spade', 'club'] # 定义了一个新列表suits
>>> nest = list(suits)  # 复制列表suits的值, 并与nest绑定
>>> nest[0] = suits     # 把列表nest的第一个元素改成suits的值
```

!(image)[https://wizardforcel.gitbooks.io/sicp-in-python/content/img/lists.png]

nest形成的是一个全新的列表, 对nest的改变并不会影响到suits, 因为两个列表可能有相同的内容,但实际上是不同的列表, 所以我们需要一种方法来检测是否两个对象都是相同的. Python 提供了两个比较运算符, is 和 is not, 它可以测试两个表达式的求值结果是否为相同的对象, 如果两个对象在其当前值中相等, 并且对其中的任何更改都将始终反映在另一个中, 则它们是相同的.**身份是比平等更强的条件.**

```python

>>> suits == ['heart', 'diamond', 'spade', 'club'] 
True
>>> suits is ['heart', 'diamond', 'spade', 'club'] 
False

# 第一个语句右边的列表是一个全新的列表, 它与suits有相同的值, 所以它们是平等的
# 但是它们有各自的身份, 改变一个列表并不会影响到一个列表. 所以它们的身份不一样
```

列表推导式: 使用扩展语法来创建列表, 类似于生成器表达式的语法(包含一个表达式，后跟一个for子句，然后是零个或多个for或if子句的括号)
```python
l1 = [(i,j) for i in range(10)  for j in range(5) if i > 3 ]
l2 = [(i,j) for i in range(10)  if i > 3 for j in range(5) ]

l3 = [(i, j, k) for i in range(10) if i % 2 ==0 for j in range(5) if j > 3 for k in range(10) if i >5]
```


通过函数实现列表:
```python
>>> def make_mutable_rlist():
        """Return a functional implementation of a mutable recursive list."""
        contents = empty_rlist
        def dispatch(message, value=None):
            nonlocal contents
            if message == 'len':
                return len_rlist(contents)
            elif message == 'getitem':
                return getitem_rlist(contents, value)
            elif message == 'push_first':
                contents = make_rlist(value, contents)
            elif message == 'pop_first':
                f = first(contents)
                contents = rest(contents)
                return f
            elif message == 'str':
                return str(contents)
        return dispatch
```


--- 

面向对象编程（OOP）是一种用于组织程序的方法,就像抽象数据类型那样,对象创建了数据使用和实现之间的抽象界限.类似消息传递中的分发字典,对象响应行为请求.就像可变的数据结构,对象拥有局部状态,并且不能直接从全局环境访问.Python 对象系统提供了新的语法,更易于为组织程序实现所有这些实用的技巧.


类用作所有类型为该类的对象的模板, 每个对象都是某个特定类的实例.

一个类允许我们创建多个实例, 创建一个新的对象实例的行为被称为实例化类.

对象的属性是与该对象关联的名称-值对, 可通过点表示法访问它, 属性是具体到一个特定的对象的,而不是类的所有对象,它被称为实例属性, 同时实例属性也可以称为字段、属性或实例变量.

操作对象或执行特定于对象的函数称为方法. 方法的副作用和返回值可以依赖和更改对象的其他属性.

我们可以这样定义类:
```python
class <name>(<base class>):
    <suite>
```

当一个类语句执行时, 会创建一个新类与name所绑定在当前环境下的第一帧. 然后执行suite. 任何name绑定在& lt;suite&gt;类的声明,通过def或赋值语句,创建或修改属性的类, 在类语句的suite里边绑定的name, 无论是通过def还是赋值语句绑定, 执行的都是创建或修改的操作.


初始化方法: __init__

构造函数: __new__

访问类的属性:
```python
<expression> . <name>
```

我们通过'.'符号来访问类的属性(方法也是属性), 左边表达式返回的必须是一个类, 而右边的name只能是一个简单的名称而不能是其它的任何表达式

当调用一个对象的方法时, 将隐式地把该对象作为第一个参数传递给方法.

类属性定义在类语句的suite中, 并在所有方法的定义外, 类属性是所有对象共享的, 同时类属性也可以称为类变量或静态变量.

点表达式的求值:
```python
<expression>.<name>
```
1. 求出expression的值到点的左侧, 从而生成点表达式的对象
2. 把name该对象的实例属性相匹配;如果具有该名称的属性存在, 则返回它的值
3. 如果name不存在于实例属性，那么会在类中查找name，这会产生类的属性值
4. 这个值被返回,除非它是一个函数,在这种情况下,返回一个绑定的方法.

在其左侧包含点表达式的所有赋值语句都将影响该点表达式的对象的属性. 如果对象是实例, 则赋值设置实例属性。如果对象是类, 则赋值设置类属性。此规则的结果是, 对对象属性的赋值不能影响其类的属性.

已经重载的属性还可以通过类对象访问, 如下:

```python
class A:
    num = 1 
    
    
class B(A):
    num = 2 
    print(num)
    print(A.num)
```

当 Python 解析不是实例属性的点表达式中的名称时, 它在类中查找名称.实际上, 在类中 查找"名称的行为,会在原始对象的类的继承链中的每个基类中查找该名称.

1. 如果它是该类中命名的属性, 则返回属性值
2. 否则, 在基类中查找名称 (如果有的话).

当子类的属性与父类属性名称一样时, 会发生重载, 已重载的属性依然可以通过类的对象来访问.

多重继承的查找顺序, 按照__mro__ 从左往右

属性本身是被存储在一个叫attributes的本地字典中的.

通过函数实现类的实例化:
```python
def make_instance(cls):
    """Return a new object instance, which is a dispatch dictionary."""
    def get_value(name): # 获取属性的方法
        if name in attributes: # 先从市里本身找, 找到属性直接返回
            return attributes[name]
        else: # 找不到就到类里边找
            value = cls['get'](name)
            return bind_method(value, instance)
    def set_value(name, value): # 设置属性的方法
        attributes[name] = value # 直接把属性设置到attributes字典里
    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance
        
        
def bind_method(value, instance):
    """Return a bound method if value is callable, or value otherwise."""
    # 如果value是function, 则把绑定方法返回, 否则直接返回value
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value
```


