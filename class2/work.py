#!/usr/bin/env python
# -*- coding:utf-8 -*-
#arthur:Dear
#2017-07-26 17:36:20


from fractions import Fraction
from collections import namedtuple,deque,OrderDict,defaultdict


#1、大小写字母a-z，生成一个列表，不能直接赋值。
list1 = [chr(i) for i in range(97,123)]

#2、复杂的列表分析时，if可以写在哪个地方的所有情况。
#A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses
#列表解析包含一个包含一个表达式，后跟一个for子句，然后是零个或多个for或if子句的括号
list2 = [i for i in range(10) if i % 2 ==0]
list3 = [i+j for i in range(10) for j in range(5) if j > 3]
list4 = [i+j for i in range(10) if i > 3 for j in range(5)]
list5 = [i+j for i in range(10) for j in range(5) if i > 3]#等于list4
list6 = [i+j for i in range(10) if i > 5 for j in range(5) if j > 3]
list7 = [i+j for i in range(10) for j in range(5) if i > 5 if j > 3 if i+j <13]
list8 = [i+j+k for i in range(10) if 3 < i < 8   if i % 2 == 0 for j in range(100,110) for k in range(10,20,2) ]

#3、练习删除一个列表 del a  |  del a[:]
a = [i for i in range(10)]
b = a
#id(a) == id(b)
del a #del a 实际上只是把a变量删掉 而不会修改A指向的内存地址的值,而b还是可以指向原本的内存地址,所以b的值不会变
del a[:]#del a[:] 就是把变量a所指向内存地址的值给改了,因为a与b是指向同一个内存地址,所以b的值也会跟着变

#4、整数 浮点数 小数 分数 复数 字符串 list tuple set dict namedtuple deque OrderDict defaultdict
#初始化并且列出所有不带双下划线的方法及作用，不同数据结构方法间的异同、总结
a = 65
a.bit_length()
'''
int.bit_length() -> int
Number of bits necessary to represent self in binary.
返回整数对应二进制的长度
bin(a) --> '0b1000001'
a.bit_length() --> 7
'''
a.conjugate()
'''
Returns self, the complex conjugate of any int
返回整数本身
a.conjugate() --> 65
'''
a.from_bytes()
'''
int.from_bytes(bytes, byteorder, *, signed=False) -> int
Return the integer represented by the given array of bytes.
将字节数组转换为整数
'''
a.imag
'''
the imaginary part of a complex number
一个属性,代表复数
'''
a.numerator()
'''
the numerator of a rational number in lowest terms

'''
a.real()
'''
the real part of a complex number
返回复数的实数部分。
'''
a.to_bytes()
'''
Return an array of bytes representing an integer.
将整数转为字节组
'''

b = float(a)
b.as_integer_ratio()
'''
Return a pair of integers, whose ratio is exactly equal to the original
float and with a positive denominator.
Raise OverflowError on infinities and a ValueError on NaNs.
将浮点数转换成分数
'''
b.conjugate()
'''
Return self, the complex conjugate of any float.
返回本身
'''
b.fromhex()
'''
Create a floating-point number from a hexadecimal string.
float.fromhex(string) -> float
将16进制的字符串转成浮点数
'''
b.hex()
'''
Return a hexadecimal representation of a floating-point number.
float.hex() -> string
将浮点数转为16禁止的字符串,与fromhex相反
'''
b.imag()
'''
the imaginary part of a complex number

'''
b.is_integer()
'''
Return True if the float is an integer.
根据浮点数能否转成整数，可以即返回True
'''
b.real()
'''
the real part of a complex number
返回复数的实数部分
'''

#from fractions import Fraction
#分数
c = Fraction(3,5)
c.conjugate()
'''
Conjugate is a no-op for Reals.
'''
c.denominator()
'''
the denominator of a rational number in lowest terms
分数的分母部分
'''
c.from_decimal()
'''
Converts a finite Decimal instance to a rational number, exactly.
将有理数转成分数
'''
c.from_float()
'''
Converts a finite float to a rational number, exactly.
将浮点数转成分数
'''
c.imag()
'''
the imaginary part of a complex number
复数的虚数部分
'''
c.limit_denominator()
'''
Closest Fraction to self with denominator at most max_denominator.

'''
c.numerator()
'''
the numerator of a rational number in lowest terms
分数的分子部分
'''
c.real()
'''
the real part of a complex number
复数的实数部分
'''

d = 1j
d.conjugate()
'''
Return the complex conjugate of its argument. (3-4j).conjugate() == 3+4j.
'''
d.imag()
'''
the imaginary part of a complex number
复数的虚数部分
'''
d.real()
'''
the real part of a complex number
复数的实数部分
'''

e = 'str'
e.capitalize()
'''
Return a capitalized version of S, i.e. make the first character have upper case and the rest lower case.
返回第一个字符为大写，其他字符为小写的字符串
'''
e.casefold()
'''
Return a version of S suitable for caseless comparisons.

'''
e.center()
'''
Return S centered in a string of length width
返回字符串本身，然后用空格填补形成居中效果
'''
e.count()
'''
Return the number of non-overlapping occurrences of substring sub in string S[start:end]
统计字符串内某个字符出现次数
'''
e.encode()
'''
Encode S using the codec registered for encoding.
将字符串以指定的字符编码进行编码
'''
e.endswith()
'''
Return True if S ends with the specified suffix, False otherwise.
判断字符串是不是以某个字符或某几个字符结尾，返回bool
'''
e.expandtabs()
'''
Return a copy of S where all tab characters are expanded using spaces.
将制表和换成空格
'''
e.find()
'''
Return the lowest index in S where substring sub is found,
字符串内查找某个字符的位置
'''
e.format()
'''
Return a formatted version of S, using substitutions from args and kwargs.
占位符替换
'''
e.format_map()
'''
Return a formatted version of S, using substitutions from mapping.
'''
e.index()
'''
Return the lowest index in S where substring sub is found,such that sub is contained within S[start:end].
按下标给出字符串中的字符
'''
e.isalnum()
'''
Return True if all characters in S are alphanumeric and there is at least one character in S, False otherwise.
判断字符串是否所有字符都为数字或字母且不为空
'''
e.isalpha()
'''
Return True if all characters in S are alphabetic and there is at least one character in S, False otherwise.
判断字符串中是否所有字符都为字母且不为空字符
'''
e.isdecimal()
'''
Return True if there are only decimal characters in S,False otherwise.
判断字符串中是只有十进制的字符
'''
e.isdigit()
'''
Return True if all characters in S are digits and there is at least one character in S, False otherwise.
判断字符串内是否所有字符都是数字
'''
e.isidentifier()
'''
Return True if S is a valid identifier according to the language definition.

'''
e.islower()
'''
Return True if all cased characters in S are lowercase and there is at least one cased character in S, False otherwise.
判断字符串内是否所有字符都为小写字母且字符不为空
'''
e.isnumeric()
e.isprintable()
e.isspace()
e.istitle()
e.isupper()
e.join()
e.ljust()
e.lower()
e.lstrip()
e.maketrans()
e.partition()
e.replace()
e.rfind()
e.rindex()
e.rjust()
e.rpartition()
e.rsplit()
e.rstrip()
e.split()
e.splitlines()
e.startswith()
e.strip()
e.swapcase()
e.title()
e.translate()
e.upper()
e.zfill()


l = [i for i in range(5)]
l.append()
l.clear()
l.copy()
l.count()
l.extend()
l.index()
l.insert()
l.pop()
l.remove()
l.reverse()
l.sort()

t = (1,3,5,7,9)
t.count()
t.index()

s = set('Dear')
s.append()
s.clear()
s.copy()
s.difference()
s.difference_update()
s.discard()
s.intersection()
s.intersection_update()
s.isdisjoint()
s.issubset()
s.issuperset()
s.pop()
s.remove()
s.symmetric_difference()
s.symmetric_difference_update()
s.union()
s.update()

d = {'a':1,'b':2}
d.clear()
d.copy()
d.fromkeys()
d.get()
d.items()
d.keys()
d.pop()
d.popitem()
d.setdefault()
d.update()
d.values()

#from collections import namedtuple
NT_Obj = namedtuple('class',['type','teacher','time'])
nt = NT_Obj(type='python',teacher='aju',time='120min')
nt.count()
nt.index()
nt.type
nt.teacher
nt.time

dq = deque([i for i in range(5)])
dq.append()
dq.appendleft()
dq.clear()
dq.copy()
dq.count()
dq.extend()
dq.extendleft()
dq.index()
dq.insert()
dq.maxlen()
dq.pop()
dq.popleft()
dq.remove()
dq.reverse()
dq.rotate()

d1 = OrderedDict({'a':1,'b':2})
d1.clear()
d1.Copy()
d1.fromkeys()
d1.get()
d1.items()
d1.keys()
d1.move_to_end()
d1.pop()
d1.popitem()
d1.setdefault()
d1.update()
d1.values()

d2 =  defaultdict(list)
d2['a'] = ['a','A']
d2['b'] = ['b','B']

d2.clear()
d2.copy()
d2.default_factory()
d2.fromkeys()
d2.get()
d2.items()
d2.keys()
d2.pop()
d2.popitem()
d2.setdefault()
d2.update()
d2.values()


#5、import前后定义函数、定义函数并调用、定义类和方法、定义类并初始化、定义类并初始化后调用方法
class Cls:

    def func(self):
        os.system('ls')

cls = Cls()#实例化成功
cls.func()#调用失败:NameError,提示os找不到，因为系统未导入

class Cls_Test:

    def __init__(self):
        os.system('ls')

cls_t = Cls_Test()#实例化失败

def func():
    os.system('ls')

func()#此次执行会NameError,提示os找不到，因为系统未导入

import os.system

cls = Cls()#执行成功
cls.func()#执行成功

cls_t = Cls_Test()#执行成功

func()#执行成功


#6、命名空间/作用域的总结

全局变量的话一般是在任何地方都可以访问到该变量,但是如果想在类或函数里边修改全局变量的值就需要使用global关键字

一般称顶格定义的变量为全局变量

而函数和类里边的变量访问1个变量时，会先从局部变量里边找，(所以局部变量的名字和全局变量的名字冲突时,会先找局部变量)
当找不到该变量的定义时就会向上一级的变量找，直至找到全局变量，还找不到就会报error

而我们可以通过locals() 和globals() 方法来查看当前变量和全局变量

而import是个例外
impoert os

def test()
    if 1:
        os.system('ls')
    else:
        import os

在这种情况下会报UnboundLocalError: local variable 'os' referenced before assignment


