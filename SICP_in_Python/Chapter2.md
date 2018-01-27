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
>>> counts = make_rlist(1, make_rlist(2, make_rlist(3, make_rlist(4, empty_rlist)))) # 相当于(1, (2, (3, (4, None))))
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
