# 常用库

## Mock

Mock是Python中一个用于支持单元测试的库，它的主要功能是使用mock对象替代掉指定的Python对象，以达到模拟对象的行为。

### mock安装

从Python 3.3开始，mock模块已经被合并到标准库中，被命名为**unittest.mock**，可以直接import进来使用

```python
from unittest import mock
```

### `Mock`对象

Mock对象就是mock模块中的一个类的实例，这个类的实例可以用来替换其他的Python对象，来达到模拟的效果。

```python
class Mock(spec=None, side_effect=None, return_value=DEFAULT, wraps=None, name=None, spec_set=None, **kwargs)
```

#### 基本用法

1. 找到要替换的对象。这个对象可以是一个类，或者是一个函数，或者是一个类实例。
2. 然后实例化Mock类得到一个mock对象，并且设置这个mock对象的行为，比如被调用的时候返回什么值，被访问成员的时候返回什么值等。
3. 使用这个mock对象替换掉想替换的对象，也就是步骤1中确定的对象。
4. 之后就可以开始写测试代码，这个时候可以保证替换掉的对象在测试用例执行的过程中行为和预设的一样。

被测模块 client.py

```python
import requests

def send_request(url):
    r = requests.get(url)
    return r.status_code

def visit_ustack():
    return send_request('http://www.ustack.com')
```

测试模块

```python
import unittest
import mock
import client

class TestClient(unittest.TestCase):

    def test_success_request(self):
        success_send = mock.Mock(return_value='200')
        client.send_request = success_send
        self.assertEqual(client.send_request(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        client.visit_ustack = fail_send
        self.assertEqual(client.visit_ustack(), '404')
```

1. 找到要替换的对象：需要测试的是`send_request`这个函数，那么我们需要替换掉`send_request`这个函数。
2. 实例化Mock类得到一个mock对象，并且设置这个mock对象的行为。在成功测试中，设置mock对象的返回值为字符串“200”；在失败测试中，设置mock对象的返回值为字符串"404"。
3. 使用这个mock对象替换掉想替换的对象。即：`client.send_request`
4. 写测试代码。调用`client.visit_ustack()`，并且期望它的返回值和预设值一样。

#### class Mock的参数

- **name**: 这个是用来命名一个mock对象，只是起到标识作用。当print一个mock对象的时候，可以看到它的name。
- **return_value**: 可以指定一个值（或者对象），当mock对象被调用时，如果side_effect函数返回的是*DEFAULT*，则对mock对象的调用会返回return_value指定的值。
- **side_effect**: 这个参数指向一个可调用对象，一般就是函数。当mock对象被调用时，如果该函数返回值不是*DEFAULT*时，那么以该函数的返回值作为mock对象调用的返回值。

## urllib库

* 生成request实例，用于模拟http请求，包括请求头、请求内容等。可以用于Post和Get请求
* response发出请求后接收到的响应信息。

### urlopen

```python
import urllib

# 向指定的url发送请求，并返回服务器响应的类文件对象
response = urllib.request.urlopen("http://www.baidu.com")

# 类文件对象支持 文件对象的操作方法，如read()方法读取文件全部内容，返回字符串
html = response.read()

# 打印字符串
print(html)
```

### Request

```python
import urllib.request

# url 作为Request()方法的参数，构造并返回一个Request对象
request = urllib.request.Request("http://www.baidu.com")

# Request对象作为urlopen()方法的参数，发送给服务器并接收响应
response = urllib.request.urlopen(request)

html = response.read()

print(html)
```

Request实例参数：

1. url地址
2. data(默认空)：是伴随 url 提交的数据比如要(post的数据)，同时HTT 请求将从"GET"方式改为"POST"方式。
3. headers(默认空)：是一个字典，包含了需要发送的HTTP报头的键值对。

#### User-Agent

浏览器信息

```python
import urllib

url = "http://www.itcast.cn"

#IE 9.0 的 User-Agent，包含在 ua_header里
ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"} 

#  url 连同 headers，一起构造Request请求，这个请求将附带 IE9.0 浏览器的User-Agent
request = urllib.request.Request(url, headers=ua_header)

# 向服务器发送这个请求
response = urllib.request.urlopen(request)

html = response.read()
print(html)
```

#### 添加更多的Header信息

在HTTP Request中加入特定的Header，来构造一个完整的HTTP请求消息。

* 添加一个特定的header

```python
import urllib

url = "http://www.itcast.cn"
header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"} 
request = urllib.request.Request(url, headers=ua_header)

#也可以通过调用Request.add_header() 添加/修改一个特定的header
request.add_header("Connection", "keep-alive")

# 也可以通过调用Request.get_header()来查看header信息
# request.get_header(header_name="Connection")

response = urllib.request.urlopen(request)

print(response.code)     #可以查看响应状态码
html = response.read()
print(html)
```

* 随机添加/修改User-Agent

```python
import urllib
import random

url = "http://www.itcast.cn"

ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
    "Mozilla/5.0 (Macintosh; Intel Mac OS... "
]

user_agent = random.choice(ua_list)
request = urllib.request.Request(url)

#也可以通过调用Request.add_header() 添加/修改一个特定的header
request.add_header("User-Agent", user_agent)

# 第一个字母大写，后面的全部小写
request.get_header("User-agent")

response = urllib.request.urlopen(request)
html = response.read()
print(html)
```

### urllib的GET和POST请求

urllib默认只支持HTTP/HTTPS的GET和POST方法

#### urllib.urlencode()

汉字需要编码成 URL编码格式，然后做为url的一部分，或者作为参数传到Request对象中:

2. urllib.parse 提供 `urlencode` 方法用来GET查询字符串的产生.
3. 解码工作可以使用urllib.parse的`unquote()`函数。

```python
import urllib.parse

word = {"wd" : "传智播客"}
# 通过urllib.urlencode()方法，将字典键值对按URL编码转换，从而能被web服务器接受。
wd = urllib.parse.urlencode(word)

# 通过urllib.unquote()方法，把 URL编码字符串，转换回原先字符串。
urllib.parse.unquote(wd)
```

#### Get方式

Get请求百度获取网页

```python
import urllib

url = "http://www.baidu.com/s"
word = {"wd":"传智播客"}

word = urllib.parse.urlencode(word) #转换成url编码格式（字符串）
newurl = url + "?" + word    # url首个分隔符就是 ?

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

request = urllib.request.Request(newurl, headers=headers)
response = urllib.request.urlopen(request)
print(response.read())
```

#### Post请求

Request请求对象的里有data参数，是Post请求参数data，data是一个字典，要匹配键值对。

```python
import urllib

# POST请求的目标URL
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

headers={"User-Agent": "Mozilla...."}

formdata = {
    "type":"AUTO",
    "i":"i love python",
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"true"
}

data = urllib.parse.urlencode(formdata).encode(encoding='UTF8')

# 有data参数，自动变为post请求
request = urllib.request.Request(url, data = data, headers = headers)
response = urllib.request.urlopen(request)
print(response.read())
```

#### 获取AJAX加载的内容

```python
import urllib

# demo1

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers={"User-Agent": "Mozilla...."}

# 变动的是这两个参数，从start开始往后显示limit个
formdata = {
    'start':'0',
    'limit':'10'
}
data = urllib.parse.urlencode(formdata).encode(encoding='UTF8')

request = urllib.request.Request(url, data = data, headers = headers)
response = urllib.request.urlopen(request)
print(response.read())

# demo2
url = "https://movie.douban.com/j/chart/top_list?"
headers={"User-Agent": "Mozilla...."}

# 处理所有参数
formdata = {
    'type':'11',
    'interval_id':'100:90',
    'action':'',
    'start':'0',
    'limit':'10'
}
data = urllib.parse.urlencode(formdata).encode(encoding='UTF8')

request = urllib.request.Request(url, data = data, headers = headers)
response = urllib.request.urlopen(request)
print(response.read())
```

### Handler处理器和自定义Opener

* opener是 urllib.request.OpenerDirector的实例，urlopen是一个特殊的opener(模块预先构建好的)。
* 基本的urlopen()方法不支持代理、cookie等其它HTTP/HTTPS高级功能。所以要支持这些功能：
  1. 使用相关的Handler来创建特定功能的处理器对象。
  2. 然后通过 `urllib.request.build_opener()`方法使用这些处理器对象，创建自定义opener对象。
  3. 使用自定义的opener对象，调用`open()`方法发送请求。

#### 简单的自定义opener()

```python
import urllib

# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
http_handler = urllib.request.HTTPHandler()

# 构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
# http_handler = urllib.request.HTTPSHandler()

# 调用urllib2.build_opener()方法，创建支持处理HTTP请求的opener对象
opener = urllib.request.build_opener(http_handler)

# 构建 Request请求
request = urllib.request.Request("http://www.baidu.com/")

# 调用自定义opener对象的open()方法，发送request请求
response = opener.open(request)

# 获取服务器响应内容
print(response.read())

# 结果urllib.request.urlopen()一样
```

如果在`HTTPHandler()`增加 `debuglevel=1`参数，还会将 Debug Log 打开。

```python
# 仅需要修改的代码部分：

# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求，同时开启Debug Log，debuglevel 值默认 0
http_handler = urllib.request.HTTPHandler(debuglevel=1)

# 构建一个HTTPHSandler 处理器对象，支持处理HTTPS请求，同时开启Debug Log，debuglevel 值默认 0
https_handler = urllib.request.HTTPSHandler(debuglevel=1)
```

#### ProxyHandler处理器

urllib中通过ProxyHandler来设置使用代理服务器。

```python
import urllib

# 构建了两个代理Handler，一个有代理IP，一个没有代理IP
httpproxy_handler = urllib.request.ProxyHandler({"http" : "124.88.67.81:80"})
nullproxy_handler = urllib.request.ProxyHandler({})

proxySwitch = True #定义一个代理开关

# 通过 urllib2.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
# 根据代理开关是否打开，使用不同的代理模式
if proxySwitch:  
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)

request = urllib.request.Request("http://www.baidu.com/")

# 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。
response = opener.open(request)

# 2. 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
# urllib2.install_opener(opener)
# response = urlopen(request)
print(response.read())
```

### Cookie

在Python处理Cookie，一般是通过`cookielib`模块和 urllib2模块的`HTTPCookieProcessor`处理器类一起使用。

* `cookielib`模块：主要作用是提供用于存储cookie的对象
* `HTTPCookieProcessor`处理器：主要作用是处理这些cookie对象，并构建handler对象。

#### cookielib 库

该模块主要的对象有CookieJar(父类)、FileCookieJar(CookieJar子类)、MozillaCookieJar(FileCookieJar子类)、LWPCookieJar(FileCookieJar子类)：

* CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。
* FileCookieJar (filename,delayload=None,policy=None)：从CookieJar派生而来，用来创建FileCookieJar实例，检索cookie信息并将cookie存储到文件中。filename是存储cookie的文件名。delayload为True时支持延迟访问访问文件，即只有在需要时才读取文件或在文件中存储数据。
* MozillaCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与`Mozilla浏览器 cookies.txt兼容`的FileCookieJar实例。
* LWPCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与`libwww-perl标准的 Set-Cookie3 文件格式`兼容的FileCookieJar实例。

1. 获取Cookie，并保存到CookieJar()对象中

```python
import urllib
import http.cookiejar

# 构建一个CookieJar对象实例来保存cookie
cookiejar = http.cookiejar.CookieJar()

# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler = urllib.request.HTTPCookieProcessor(cookiejar)

# 通过 build_opener() 来构建opener
opener = urllib.request.build_opener(handler)

# 4. 以get方法访问页面，访问之后会自动保存cookie到cookiejar中
opener.open("http://www.baidu.com")

## 可以按标准格式将保存的Cookie打印出来
cookieStr = ""
for item in cookiejar:
    cookieStr = cookieStr + item.name + "=" + item.value + ";"

## 舍去最后一位的分号
print(cookieStr[:-1])
```

2. 访问网站获得cookie，并把获得的cookie保存在cookie文件中

```python
import urllib
import http.cookiejar

# 保存cookie的本地磁盘文件名
filename = 'cookie.txt'

# 声明一个MozillaCookieJar(有save实现)对象实例来保存cookie，之后写入文件
cookiejar = http.cookiejar.MozillaCookieJar(filename)

# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler = urllib.request.HTTPCookieProcessor(cookiejar)

# 通过 build_opener() 来构建opener
opener = urllib.request.build_opener(handler)

# 创建一个请求，原理同urllib2的urlopen
response = opener.open("http://www.baidu.com")

# 保存cookie到本地文件
cookiejar.save()
```

3. 从文件中获取cookies，做为请求的一部分去访问

```python
import urllib
import http.cookiejar

# 创建MozillaCookieJar(有load实现)实例对象
cookiejar = http.cookiejar.MozillaCookieJar()

# 从文件中读取cookie内容到变量
cookie.load('cookie.txt')

# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler = urllib.request.HTTPCookieProcessor(cookiejar)

# 通过 build_opener() 来构建opener
opener = urllib.request.build_opener(handler)

response = opener.open("http://www.baidu.com")
```

#### 利用cookielib和post登录人人网

```python
import urllib
import http.cookiejar

# 1. 构建一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()

# 2. 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

# 3. 通过 build_opener() 来构建opener
opener = urllib.request.build_opener(cookie_handler)

# 4. addheaders 接受一个列表，里面每个元素都是一个headers信息的元祖, opener将附带headers信息
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]

# 5. 需要登录的账户和密码
data = {"email":"mr_mao_hacker@163.com", "password":"alaxxxxxime"}  

# 6. 通过urlencode()转码
postdata = urllib.parse.urlencode(data)

# 7. 构建Request请求对象，包含需要发送的用户名和密码
request = urllib.request.Request("http://www.renren.com/PLogin.do", data = postdata)

# 8. 通过opener发送这个请求，并获取登录后的Cookie值，
opener.open(request)                                              

# 9. opener包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response = opener.open("http://www.renren.com/410043129/profile")  

# 10. 打印响应内容
print(response.read())
```





