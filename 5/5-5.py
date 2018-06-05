# 返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 7)
print(f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())

def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count1()
print(f1())
print(f2())
print(f3())

def createCounter():
    def f():
        n = 0
        while True:
            n = n + 1
            yield n
    f = f()
    def counter():
        return next(f)
    return counter