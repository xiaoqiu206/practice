# coding=utf-8
'''
Created on 2016年6月27日

@author: qiu
'''


def add_i(func):
    def outer(content):
        content = "<i>%s</i>" % content
        print 'call func add_i'
        return func(content)
    return outer


def add_b(func):
    def outer(content):
        content = "<b>%s</b>" % content
        print 'call func add_b'
        return func(content)
    return outer


@add_i
@add_b
def div(content):
    print 'call func div'
    return "<div>%s</div>" % content


def main():
    print div("内容")

if __name__ == "__main__":
    main()
