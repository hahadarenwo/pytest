
L2 = list(range(1, 11))
print(L2)

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

L1 = [m + n for m in 'ABC' for n in 'XYZ']
print(L1)

L4 = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L4])

L6 = []
L1 = ['Hello', 'World', 18, 'Apple', None]
for n in L1:
    if isinstance(n,str):
        L6.append(n.lower())
print(L6)
if L6 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')