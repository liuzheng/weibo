weibo
=====



为方便使用合并各种文件到Lweibo.py，并且支持Python3，完全不懂的小白请修改config.ini后打开example.py按需运行，运行抓取任务时请下载完全整个文件，不要就下载一个py文件问为什么出错

关于出现`RuntimeError: 20019 repeat content!` 问题是新浪最近的小动作，抓取间隔过小会抛错，这个我没办法破

Lweibo.py 提供了API方式和模拟登录的方式，如有问题email我吧

利用python实现对新浪微博的抓取

此爬虫使用了@lxyu 的SDK https://github.com/lxyu/weibo 感谢他之前的工作

2015年08月05日 更新

支持Python3！

## TODO

~~1.模拟登录，并抓取某个页面~~

~~2.对页面解析~~

3.定时任务（已完成，毕业后放出）不放了,换代没啥意思了

4.分布式存储HBase（已完成，毕业后放出）不放了,换代没啥意思了

5.通过API调取活跃用户ID，避免自曾产生僵尸用户数据（已完成，毕业后放出）不放了,换代没啥意思了


3,4,5 三点架构早就变了,觉得大家都可以写写吧,现在可以使用 Elasticsearch 去替代 HBase, 写起来比 HBase 轻松, 前端展示也很方便, 直接用 Kibana 或者 Grafana 做展示,比几年前轻松多了.
