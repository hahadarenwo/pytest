from collections import Iterable
from collections import Iterator
print(isinstance([], Iterable))#可迭代对象
print(isinstance([], Iterable))#可迭代器 可被next()函数调用

for x in [1, 2, 3, 4, 5]:
    pass
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
    except StopIteration:
        #遇到StopIteration就退出循环
        break