# coding=utf-8
'''
Created on 2016年5月1日
用装饰器创建property
@author: xiaoq
'''


class Foo(object):

    @property
    def foo(self):
        "首先我们装饰了foo方法,使他成为getter"
        return self._foo

    @foo.setter
    def foo(self, value):
        """
        这个语法看起来有点奇怪,这个新方法的名字和刚装饰过的foo竟然一样!
        记住,property函数返回的是一个对象,这个对象被自动设置拥有一个setter属性,
        而这个setter属性可以被设置成为一个装饰器去装饰其他的函数
        对get和set方法使用相同的名字不是必须的,
        但是这确实可以帮助我们把多个方法组合起来成为一个property
        """
        self._foo = value


def main():
    pass


if __name__ == "__main__":
    main()