def power(x,n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s

print(power(5, 2))
print(power(5, 3))

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum