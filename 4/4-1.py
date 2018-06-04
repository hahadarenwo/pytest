
L = ['hello','world','me','you','text']
print(L[0:3])
print(L[1:3])
print(L[-2:])

L1 = list(range(100))
print(L1[:10])
print(L1[-10:])
print(L1[10:20])
print(L1[:10:2])
print(L1[::5])
print(L1[:])

L2 = 'ABCDEFG'
print(L2[:3])
print(L2[::2])


#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim1(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

def trim(s):
    if s.startswith(' '):
        s = s[1:]
        s = trim(s)
    if s.endswith(' '):
        s = s[:-1]
        s = trim(s)
    return s


print(trim('hello  '))
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')