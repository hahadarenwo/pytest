import time
def now():
    print('2015-3-25')
f = now
f()

print(now.__name__) #__name__可以获取函数的名字 注意是二个下划线

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

now()


def metric(fn):
    def demo(args, **kwargs):
        start=time.time()
        res=fn(args, **kwargs)
        stop=time.time()
        alltime=stop-start
        print('%s executed in %s ms' % (fn.name, str(alltime)))
        return res
    return demo
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

