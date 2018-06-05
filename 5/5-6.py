list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

#匿名函数
f = lambda x: x * x
print(f(2))

def build(x,y):
    return lambda: x * x + y * y