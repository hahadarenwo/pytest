from functools import reduce
import math


def add(x, y):
    return x + y


result = reduce(add, [1, 3, 5, 7, 9])
print(result)  # 可以用sum()函数替代这个功能


# 但是要变成13579可以使用reduce
def add(x, y):
    return x * 10 + y


result = reduce(add, [1, 3, 5, 7, 9])
print(result)


def fn(x, y):
    return x * 10 + y


def charToNum(s):
    digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digit[s]


print(reduce(fn, map(charToNum, '13579')))


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 作业
def normalize(name):
    name = name[0:1].upper() + name[1:len(name)].lower()
    return name


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    def s(x, y):
        return x * y

    return reduce(s, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float1(s):
    def text(x):
        DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return DIGITS[x]
    lis = s.split('.')
    num1 = reduce(lambda x, y: x * 10 + y, map(text, lis[0] + lis[1]))
    return num1/math.pow(10, len(lis[1]))


def str2float(s):
    return float(s)
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
