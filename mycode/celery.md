Celery+RabbitMQ快速入门
======
[参考链接](http://www.zeuux.com/blog/content/3938/)

本文主要介绍Celery+RabbitMQ的入门知识

Celery 是一个异步任务队列/基于分布式消息传递作业队列，它侧重于实时操作，同样也支持调度

RabbitMQ为应用程序提供了强大的消息服务。它很容易使用，适合在云规模应用，并支持所有主流的操作系统和开发平台。RabbitMQ在Mozilla公共许可下开源


# 安装Celery

使用easy_install安装

sudo easy_install Celery

# 安装RabbitMQ

在ubuntu下使用apt-get方式安装rabbitmq-server

sudo apt-get install rabbitmq-server

安装完毕之后可以使用如下命令查看MQ当前服务状态

> alex@alex-pc:~/test$ sudo rabbitmqctl status
>
> [sudo] password for alex:
> Status of node 'rabbit@alex-pc' ...
> [{running_applications,[{rabbit,"RabbitMQ","1.7.2"},
>                         {mnesia,"MNESIA  CXC 138 12","4.4.12"},
>                         {os_mon,"CPO  CXC 138 46","2.2.4"},
>                         {sasl,"SASL  CXC 138 11","2.1.8"},
>                         {stdlib,"ERTS  CXC 138 10","1.16.4"},
>                         {kernel,"ERTS  CXC 138 10","2.13.4"}]},
>  {nodes,['rabbit@alex-pc']},
>  {running_nodes,['rabbit@alex-pc']}]
> ...done.

# 使用

## 配置Celery

选择一个测试目录，在当前路径下新建配置文件celeryconfig.py,如下：

> import sys
> import os
> sys.path.insert(0, os.getcwd())
>
> CELERY_IMPORTS = ("tasks", )
>
> CELERY_RESULT_BACKEND = "amqp"
> 
> BROKER_HOST = "localhost"
> BROKER_PORT = 5672
> BROKER_USER = "guest"
> BROKER_PASSWORD = "guest"
> BROKER_VHOST = "/

## 任务代码

新建tasks.py,如下:

> from celery.task import task
> 
> @task
> def add(x, y):
>     return x + y

## 启动celery服务

在终端中使用如下命令：

> alex@alex-pc:~/test$ celeryd --loglevel=INFO
> [2011-07-28 23:06:27,226: WARNING/MainProcess]
> 
>  -------------- celery@alex-pc v2.2.7
> ---- **** -----
> --- * ***  * -- [Configuration]
> -- * - **** ---   . broker:      amqplib://guest@localhost:5672/
> - ** ----------   . loader:      celery.loaders.default.Loader
> - ** ----------   . logfile:     [stderr]@INFO
> - ** ----------   . concurrency: 2
> - ** ----------   . events:      OFF
> - *** --- * ---   . beat:        OFF
> -- ******* ----
> --- ***** ----- [Queues]
>  --------------   . celery:      exchange:celery (direct) binding:celery
>
>
> [Tasks]
>   . tasks.add
>
> [2011-07-28 23:06:27,233: INFO/PoolWorker-1] child process calling self.run()
> [2011-07-28 23:06:27,235: INFO/PoolWorker-2] child process calling self.run()
> [2011-07-28 23:06:27,236: WARNING/MainProcess] celery@alex-pc has started.

## 调用

打开ipython或者任何python shell即可

> In [8]: from celery.task import task
> 
> In [9]: import tasks
> 
> In [10]: res = tasks.add.delay(2,2)
> 
> In [11]: res.ready()
> Out[11]: True
> 
> In [12]: res.result
> Out[12]: 4

从celeryd的loginfo的输出信息中可以看到调用成功:

> [2011-07-28 23:06:39,081: INFO/MainProcess] Got task from broker: tasks.add[82d8c609-2cac-47e8-be20-eb6a2dc502d6]
> [2011-07-28 23:06:39,120: INFO/MainProcess] Task tasks.add[82d8c609-2cac-47e8-be20-eb6a2dc502d6] succeeded in 0.0137050151825s: 4
