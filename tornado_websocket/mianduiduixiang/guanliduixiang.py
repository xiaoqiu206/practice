# coding=utf-8
'''
Created on 2016年5月1日
管理对象
设计更高级别的对象:一种用来管理其他对象的对象.这种对象可以将一起都绑在一起
@author: xiaoq
'''
import sys
import os
import shutil
import zipfile


class ZipReplace(object):
    """
    在ZIP压缩文件里实现查找和替换操作的程序.
    管理对象将会负责的,就是确保下面3个步骤能够按照顺序发生:
    1. 解压缩文件
    2. 执行查找和替换动作
    3. 压缩这些新文件
    这个类初始化时以一个.zip的文件名和查找,替换字符串作为参数.
    我们创建一个临时的目录存储这些解压缩后的文件,而文件夹本身可以保持不变
    我们还要为内部添加一个实用的助手方法,用来帮助确认目录中每个文件都有独立的文件名
    """

    def __init__(self, filename, search_string, replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_diretory = "unzipped-{}".format(filename)

    def _full_filename(self, filename):
        return os.path.join(self.temp_diretory, filename)

    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        "将压缩文件解压到临时目录"
        os.mkdir(self.temp_diretory)
        zip = zipfile.ZipFile(self.filename)
        try:
            zip.extractall(self.temp_diretory)
        finally:
            zip.close()

    def find_replace(self):
        "遍历临时目录下的文件,读取每个文件的内容,替换掉指定内容,将新内容写入"
        for filename in os.listdir(self.temp_diretory):
            with open(self._full_filename(filename)) as f:
                contents = f.read()
                contents = contents.replace(
                    self.search_string, self.replace_string)
            with open(self._full_filename(filename)) as f:
                f.write(contents)

    def zip_files(self):
        f = zipfile.ZipFile(self.filename, 'w')
        for filename in os.listdir(self.temp_diretory):
            f.write(self._full_filename(filename), filename)
        shutil.rmtree(self.temp_diretory)


def main():
    z = ZipReplace('1.txt', 'abc', 'cba')
    z.zip_find_replace()

if __name__ == "__main__":
    main()
