# TaskManager

![](image/logo.png)

![PyPI](https://img.shields.io/pypi/v/spideradmin.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/SpiderAdmin)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/SpiderAdmin)
![PyPI - License](https://img.shields.io/pypi/l/SpiderAdmin)

- github: https://github.com/Adam0429/TaskManager


## 功能介绍
1. 提供一个平台对任务进行管理，可以实现新增，删除，执行，暂停，重启，定时任务。

2. 设置（定时）任务，支持2种方式
- 单次运行 
- 定时运行 每天定时运行
- 间隔运行 间隔一段时间运行

3.邮件提示报错
## 启动运行

```
在此目录下

配置default_config.conf

$ python3 manager.py       # 启动服务

```
访问：
http://127.0.0.1:5000/


## TODO
1. 将每个task的配置写进文件进行持久化（定时）
2. ~~完善task的运行暂停部分，做到兼容定时任务~~
3. 调度课程学习
4. 阅读redis调度源码
5. 做nginx认证,支持分布式多机部署
6. ~~测试爬虫源码的可用性~~
7. ~~mqtt在flask模块启动一直提示重新连接服务器，最后发现是app debug参数造成的~~

## 更新日志

| 版本 | 日期 | 描述|

|1.0 | 2021-02-19 | 测试版本 |

## 技术介绍

基于多线程和消息队列进行任务的调度管理。




