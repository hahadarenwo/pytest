# filter函数 作用原理和map一样 除了返回需要判断true和false

def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1,2,4,5,6,9,10,15])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A','','B',None,'C',''])))

#求素数 埃氏筛法
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n #生成一个奇数序列，因为偶数必然不是素数
def _not_divisible(n):
    return lambda x: x % n > 0#筛选函数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
for n in primes():
    if n < 100:
        print(n)
    else:
        break

def is_palindrome(n):
    m = str(n)
    return  m == m[::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')