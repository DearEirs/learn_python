# 用代码来验证课程所讲内容

### 函数的意义
```
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

result = send_mail('369574757@qq.com', '123456', ['369574757@qq.com'],  'Hello World')
print(result)

def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int: 
def func(x, y:int=3 z=1, *args, **kwargs) -> int:
    ''' function func
    
    :param x: bla x
    :type x: str
    '''

    return x+y+z

# 函数的传参方式 按绑定关系传递
s = "dear"

def func(s, l):
  print(id(s),s)
  s.replace('e','d')
  print(id(s),s)
  s += "Eirs"
  print(id(s),s)


def func(x, y, z):
  return x-y+z
  
func(1, 2, 3) #在第一、二、三位的参数1,2,3分别对应着参数x,y,z 所以叫按位置传参

#作用域

'''
全局作用域：在当前py文件里都生效
局部作用域：从函数或类的定义开始到该函数或类最后1行代码 为该函数或类的 局部作用域
全局变量：定格定义的变量（包含定格的if while for try里边定义的变量），在全局生效
局部变量：在函数或类里边所定义的变量，只在该函数或类中生效
'''

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

'''

'''


# 生命周期
# 变量的生命周期
a = 10000
sys.getrefcount(a) -> 2
del a
sys.getrefcount(a) -> 1
#变量a的生命周期结束,如果不del a   那么变量a 将会一直存在 直至程序关闭

#函数的生命周期
def func(x,y,z):
  total = x + y + z
  print(total)
  return total
  
#从函数第一行开始 到函数 return 返回值 若没return则到函数代码里的最后1行执行结束  即为函数的生命周期

#对象的生命周期
