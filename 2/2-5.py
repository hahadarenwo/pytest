names = ['hello','world','web']
for name in names:
    print(name)

sum = 0
for x in range(101):#range(x) 提供0-x之间的整数
    sum = sum + x
print(sum)

sum1 = 0
n = 99
while n > 0:
    sum1 = sum1 + n
    n = n - 2
print(sum1)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello, ' + x + '!')