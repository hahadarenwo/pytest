import functools
#偏函数
def int2(x,base=2):
    return int(x,base)
print(int2('1000000'))

int2 = functools.partial(int, base = 2)#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()

