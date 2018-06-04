import math
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-10))

def nop(): #如果没想好函数怎么写 可以扔一个pass先跑起来
    pass
age = 10
if age > 18:
    pass

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-1))

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = x - step * math.sin(angle)
    return nx, ny


x, y  = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)#其实返回的是一个tuple

def quadratic(a, b, c,):
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    if (b*b-4*a*c) > 0 or a != 0:
        return (x1,x2)
    else:
        return ('无解')
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
