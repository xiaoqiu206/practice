# coding=utf-8
'''
Created on 2016年7月9日

@author: qiu
'''
from collections import namedtuple

websites = [
    ('Sohu', 'http://www.sohu.com', u'张朝阳'),
    ('Sina', 'http://www.sina.com', u'王志东'),
    ('163', 'http://www.163.com', u'丁磊')
]
Website = namedtuple('Website', ['name', 'url', 'founder'])

for website in websites:
    website = Website._make(website)
    # print website

'''
打印的结果    
Website(name='Sohu', url='http://www.sohu.com', founder=u'\u5f20\u671d\u9633')
Website(name='Sina', url='http://www.sina.com', founder=u'\u738b\u5fd7\u4e1c')
Website(name='163', url='http://www.163.com', founder=u'\u4e01\u78ca')
'''

###########
# 双端队列deque: double-ended quene
# 实现了从队列头部快速增加和取出对象:.popleft(), .appendleft()
# list对象也有这2种方法,但是时间复杂度是O(n),而deque对象则是O(1)的复杂度,
##########
import sys
import time
from collections import deque

fancy_loading = deque('>--------------')


def paomadeng():
    while 1:
        print '\r%s' % ''.join(fancy_loading),
        fancy_loading.rotate(1)
        sys.stdout.flush()
        time.sleep(0.08)

print fancy_loading
# paomadeng()


#########
# 计数器是一个非常常用的功能需求,collections也贴心的提供了这个功能
########
from collections import Counter

s = "A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages."
c = Counter(s)
# 获取出现频率最高的5个字符
print c.most_common(5)


#########
# OrderedDict,排序的字典
########
from collections import OrderedDict

items = (
    ('A', 1),
    ('B', '2'),
    ('C', 3)
)

regular_dict = dict(items)
ordered_dict = OrderedDict(items)

print 'Regular Dict:'
for k, v in regular_dict.items():
    print k, v

print 'Ordered Dict:'
for k, v in ordered_dict.items():
    print k, v


from collections import defaultdict

members = [
    ['male', 'John'],
    ['male', 'Jack'],
    ['female', 'Lily'],
    ['male', 'Pony'],
    ['female', 'Lucy'],
]
result = defaultdict(list)
for sex, name in members:
    result[sex].append(name)
print result