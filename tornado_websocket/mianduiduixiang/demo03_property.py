# coding=utf-8
'''
Created on 2016年5月1日
一个使用property的更实际的例子
假如有一个定制化行为的普遍需求,他需要对那些难以计算或是查找起来花费过大的值(例如一个网络请求或是数据库查询)进行缓存
我们的目的是在本地存储这个值以避免重复调用那些花费过大的计算
@author: xiaoq
'''
import urllib
import time


class WebPage(object):

    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print "get new page"
            self._content = urllib.urlopen(self.url).read()
        return self._content


def main():
    webpage = WebPage("http://www.qq.com/")
    now = time.time()
    content1 = webpage.content
    now1 = time.time()
    print now1 - now
    content2 = webpage.content
    now2 = time.time()
    print now2 - now1
    print content1 == content2


if __name__ == "__main__":
    main()
