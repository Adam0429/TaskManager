# TaskManager

![](images/logo.png)

![PyPI](https://img.shields.io/pypi/v/spideradmin.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/SpiderAdmin)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/SpiderAdmin)
![PyPI - License](https://img.shields.io/pypi/l/SpiderAdmin)

- github: https://github.com/Adam0429/TaskManager

- 轻量级调度系统,基于python多线程和消息队列进行任务的调度管理,前端基于react。

## 功能介绍
1. 提供一个平台对任务进行管理，可以实现新增，删除，执行，暂停，重启，定时任务。

2. 支持异步调用

3. 设置（定时）任务，支持3种方式
- 单次运行 
- 定时运行 每天定时运行
- 间隔运行 间隔一段时间运行

4. 邮件提示报错

5. 运行日志

## 网页截图
![](images/demo.png)

## 架构图
![](images/架构图.png)


## 配置default_config.conf

```
[mqtt]
server=127.0.0.1  
port=1883
# mqtt的域名和端口号，如mqtt服务器不可用，运行后会报错或一直重试connected
[consumer]
log=on
email=on
# 是否开启log和email服务
[email]
account=example@qq.com
password=examplepassword
server=smtp.qq.com
receivers=['example2@qq.com']
# 用于发邮件的配置

## 在mac上启动运行

进入在此目录下

sh ./deploy.sh

访问：
http://127.0.0.1:8000/
```

## 部署在docker

```
docker image build -t taskmanager-docker .   # 根据Dockerfile创建镜像

docker images   # 查看本机镜像,检查taskmanager-docker是否创建成功

docker run -it -p 8000:8000 taskmanager-docker  # 创建容器并进入

sh ./deploy.sh

访问：
http://127.0.0.1:8000/

```

## 运行部署react前端

```
cd frontend

create-react-app my-app

将 frontend/package.json 和 frontend/src 替换掉my-app的中对应文件

cd my-app

npm install # 安装依赖

npm start

访问：
http://127.0.0.1:3000/

```

## 按照模板编写task

只需在py文件中包含run()方法即可。系统会默认调度run方法
task例子:
```
import time
def run():
    """这里是f2函数"""
    for i in range(100):
        if i == 2:
             raise Exception('错误1！！')
        time.sleep(1)
```
task例子(带可选参数):
```

import time
def run(a):
    """这里是f2函数"""
    for i in range(10):
        time.sleep(1)
        print(a)
```

## TODO
1. 将每个task的配置写进文件进行持久化（定时）
2. ~~完善task的运行暂停部分，做到兼容定时任务~~
3. 调度课程学习
4. 阅读redis调度源码
5. 做nginx认证,支持分布式多机部署
6. ~~测试爬虫源码的可用性~~
7. ~~mqtt在flask模块启动一直提示重新连接服务器，最后发现是app debug参数造成的~~
8. ~~在配置邮箱账号出错时继续运行，并记录到日志。~~
9. 根据warning,error,info等级别，对日志模块进行改进
10. ~~制作docker镜像~~
11. ~~自己搭建mqtt服务器~~
12. 设计前端页面
13. 在网页端实现配置，查看日志等操作
14. ~~测试中，一天后邮件功能失效(try except重连)~~
15. ~~测试中，60秒后所有producer全部断连。后来发现是因为keepalive机制：在 1.5*Keep Alive 的时间间隔内，如果 Broker 没有收到来自 Client 的任何数据包，那么 Broker 认为它和 Client 之间的连接已经断开。用loop_start(不堵塞当前线程)或者loop_forever(阻塞当前线程)可以自动断线重连。~~
## 更新日志

| 版本 | 日期 | 描述|

|1.0 | 2021-02-19 | 测试版本 |

|2.0 | 2021-06-02 | react版前端 |

    





