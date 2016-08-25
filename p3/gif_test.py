# coding=utf-8
'''
Created on 2016年8月25日
解析gif图,逐帧输出
@author: qiu
'''
import os.path

from PIL import Image


def gif2images(filename, dist_dir='.', _type='bmp'):
    if not os.path.exists(dist_dir):
        os.mkdir(dist_dir)
    im = Image.open(filename)
    im.seek(0)
    cnt = 0
    _type = _type.lower()
    mode = 'RGB'
    if _type == 'bmp' or _type == 'png':
        mode = 'P'
    im.convert(mode).save(dist_dir + '/%d.' % cnt + _type)
    cnt = cnt + 1
    try:
        while 1:
            im.seek(im.tell() + 1)
            im.convert(mode).save(dist_dir + '/%d.' % cnt + _type)
            cnt = cnt + 1
    except EOFError:
        pass
    white = (255, 255, 255)
    perIm = Image.open(dist_dir + '/%d.' % 0 + _type).convert('RGB')
    size = perIm.size
    prePixs = perIm.load()
    for k in range(1, cnt):
        im = Image.open(dist_dir + '/%d.' % k + _type).convert('RGB')
        pixs = im.load()
        for i in range(size[0]):
            for j in range(size[1]):
                if pixs[i, j] == white:
                    pixs[i, j] = prePixs[i, j]
        perIm = im
        im.convert(mode).save(dist_dir + '/%d.' % k + _type)
    print filename, 'split to directory: ', dist_dir
    return cnt

if __name__ == '__main__':
    frames = gif2images('1.gif', 'png', _type='png')
