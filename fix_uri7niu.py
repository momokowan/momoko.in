# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''自动生成所有目录的 index.html
Version:
    + 13.4.18 增补meta 停息,以免乱码
    + 13.4.17 增补多层目录中的目录/文件链接 (7牛没有目录概念)
    + 13.4.11 可用
'''
import os
import sys

def fixall(p2md):
    print p2md
    print os.listdir(p2md)
    for md in os.listdir(p2md):
        _page = '%s/%s'% (p2md,md)
        _remd = ''
        for line in open(_page,'r').readlines():
            #print line
            if "](http://zoomquiet.qiniudn.com" in line:
                _rel = line.replace('zoomquiet.qiniudn.com'
                                   , 'momoko.zoomquiet.top')
                print "{} \n==>\n {}".format(line, _rel)
                _remd += _rel
            else:
                _remd += line
        open(_page,'w').write(_remd)
        print "fixed -> %s "% _page

if __name__ == '__main__':
    if 2 != len(sys.argv) :
        print '''Usage:
fix_uri7niu.py /path/2/原文章目录
        '''
    else:
        startPath = sys.argv[1]
        fixall(startPath)
        print "fixall -> %s "% startPath


