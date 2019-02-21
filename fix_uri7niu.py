# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''自动批量修改因 7niu CDN 域名变更引发的图片引用失效问题
- 目前只能指定目录, 修改目录中所有 .md
- 将来看情况是否复杂到值得交互式指定目录/替换 URI 之类...
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


