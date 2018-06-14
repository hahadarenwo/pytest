#使用模块

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test model'

__author__ = 'litash feng'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()


#_XXX和__XXX之类的变量是非公开变量  但abc x123之类的为公开变量
#__name__之类的为特殊变量 一般自己不用。

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

#我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，
# 调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。WS