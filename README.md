wei-dev
=======

一个微信公众号服务本地调试工具，免去你将公众号服务部署到公网的麻烦

## 它做什么？

+ 本地生成微信服务端请求，帮助你调试你的微信公众号服务端
+ 消息模板，预置了几种消息模板，你可以选择后随意修改，然后发送到你的测试服务器。
+ 图形界面（Qt4）/ 友好的 CLI 支持 /作为单元测试的库引用
+ 支持自定义消息内容，包含openid之类，当然也可以用来测试微信服务器的模拟session之类的功能

## 快速开始

**Note** : 调试工具不带签名功能，请注意在调试的时候根据DEBUG标签关闭签名校验

```
# 安装
pip install wei-dev

# 发送一条文本消息
python -m wei_dev cli http://localhost:8001/wechat/ text  "xq 111"
```

## 图形界面调试工具

GUI程序使用pyqt4构建的,你需要用你喜欢的方式安装PyQt4

```bash
apt-get install python-qt4
# or 
pip install PyQt4
```
然后，运行
```bash
python -m wei_dev gui
```

如果你的PyQt已经安装完毕，应该会出现如下界面：），Just enjoy it

![weidev.png](weidev.png)

## 作为库引用

TODO

目前需要你自己去`wei_dev.sender` 阅读源码：）


## Change Log
- 2017-07-04
  + 重构代码结构，新增包 `wei-dev` 并上传到pypi
  + 增加 CLI 工具，并修改CLI和GUI版本的运行方式
- 2014-07-15 damonchen 君更正的数据发送类型
- 2014-05-10 修正了在eclipse中启动可以发送中文而在shell中启动无法发送中文的问题
- 2014-05-09 first release maybe for last.

## FAQ
+ GUI为何偶尔会卡住，程序动不了了？    
那是因为urllib2正在打开url,阻塞了程序，由于简单起见并没有使用线程，遇到卡顿请等待一会，会响应的:)

## 说明

如果你觉得这个小程序有用，请给我一个赞……（啊？好像没发现哪里有赞啊……嗯嗯……不要在意这些细节
另外第一次用pyqt，代码很丑，欢迎各种更改代码结构和添加功能，pull request你值得拥有：）



## 关于

我的[Github](https://github.com/winkidney)
我的[BLOG](http://blog.slassgear.com)

