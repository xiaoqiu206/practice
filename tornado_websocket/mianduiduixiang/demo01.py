# coding=utf-8
'''
Created on 2016年4月30日
半私有变量,getter,setter和property
@author: xiaoq
'''


class Color(object):

    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if name == "Invalid Name":
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name
    # property函数实际上返回了一个对象,
    # 该对象通过我们指定的方法代理了全部属性值访问或赋值的请求
    name = property(_get_name, _set_name)


def main():
    c = Color("#996600", 'a color')
    print c.name
    c.name = "red"
    print c.name
    c.name = "Invalid Name"
    print c.name

if __name__ == "__main__":
    main()
