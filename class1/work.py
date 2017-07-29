#!/usr/bin/env python
# encoding: utf-8

#python语法文档:https://github.com/python/cpython/blob/master/Grammar/Grammar

import math
import math as m, os
from os import path
from os.path import sys,getctime
from os import (path,sys,)
from . import mymodules
from .. import mymodules


#装饰器
@decorator
class Descorator_Test:
    pass

@decorator(x,y):
def Descorator_Test:
    pass

@decorator
@decorator(x=1, y=2):
async def Descorator_Test:
    pass

@decorator(x, *args, y, **kwargs)
@decorator(x=1, *, y=2):
async def Descorator_Test:
    pass

@decorator(*args, y, **kwargs)
@decorator(y, **kwargs):
async def Descorator_Test:
    pass

@decorator(**kwargs):
async def Descorator_Test:
    pass

#函数
def func():
    pass

def func(arg1, arg2):
    pass

def func(arg1, *, arg2):
    pass

def func(arg1, arg2, *):
    pass

def func(arg1:int, *, arg2:str=1, **) -> bool:
    pass

def func(arg1, *args, **kwargs):
    pass

def func(arg1, **):
    pass

def func(*, arg **):
    pass

def func(*, **):
    pass

def func(**):
    pass

#类
class MyClass:
    pass

class MyClass(arg1,arg2=2,*args,**kwargs):
    pasas


#ASYNC函数
async + 函数
async + while
async + for

#if
if 1==1:
    pass

if 1==1 or 1==2:
    pass
else:
    pass

if 1==1 and 1==2:
    pass
elif:
    pass
else:
    pass

#while
while True:
    pass

while True:
    pass
else:
    pass

#for
for i in range(10):
    pass

for i in range(10):
    pass
else:
    pass

#try
try:
    pass
except:
    pass

#所以, try: 危险语句，except：危险发生了怎么办，else:危险没发生怎么办
try:
    pass
except ImportError as e:
    pass
else:
    pass

try:
    pass
except ImportError as e:
    pass
else:
    pass
finally:
    pass

try:
    pass
except ImportError as e:
    pass
finally:
    pass

#with
with open(r'file','w'):
    pass

with open(r'file','w'), open(r'file2','r') as f1:
    pass


#yield
yield i
yield i,j
yield from i

#lambda
l = lambda : x

l = lambda x : x

l = lambda x=1,y=2 : x + y

l = lambda x, y, * : x ** y

l = lambda x, y, *, z : str(x) + str(y) + str(z)

l = lambda x, y, *args, z, **kwargs : x

l = lambda *args, x, **kwargs : x

l = lambda x, **kwargs : x

l = lambda **kwargs : x

