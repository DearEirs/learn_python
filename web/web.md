![image](https://raw.githubusercontent.com/DearEirs/static/master/images/web.png)



在处理一个页面请求时我们一般会需要用到一下信息:
1. 请求头, 请求头里边包含了很多的信息如COOKIE、URI等. 可以协助我们处理请求
2. 提交的参数, 用户通过GET/POST请求提交上来的参数.
3. 根据1-2的输入, 进行自定义的处理过程
4. 输出html页面, 或json数据(API接口)

如何获取请求头的信息
```python
import os


# 这是返回给客户端的请求头
print("Content-type: text/html\n\n")
print(os.environ)
```

在输出界面我们就可以看到我们所提交过去的各种信息.

GET/POST的请求参数, GET的请求参数我们可以通过os.environ里的QUERY_STRING看到. 而事实上我们还可以通过CGI模块来获取

```python
import cgi


# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()
username = form.getvalue('username', default=None)
password = form.getvalue('password', default=None)

print("Content-type: text/html\n\n")
print("Your username is %s, password is %s"% (username, password))
```

> 无论是通过GET还是POST提交的参数, 都可以通过getvalue获取.

cgi是通过stdin, stdout来传递数据的.要让可执行文件的输出不止于helloworld, 那么就需要把特定的信息输出到stdout从而输出至客户端. 对于REST风格的API而言, 可以使用json.dumps来生成返回数据. 而如果是作为网页形式, 需要返回整个html, 那么我们将需要输出html的dom、css、javascript, 要我们一行一行把这些东西给输出到stdout是非常麻烦的.  这时我们就可以通过模板语言来构建html.

因为CGI会直接启动一个进程来执行脚本, 那么我们就需要注意一个安全性的问题. 执行脚本的用户应该尽量少拥有无关的权限. 以防被恶意用户利用.

