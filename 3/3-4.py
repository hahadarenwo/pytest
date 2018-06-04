def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))


def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        (move(n - 1, a, c, b))
        print(a, '-->', c)
        (move(n - 1, b, a, c))
        # print(move(n - 1, a, b, c))


move(3, 'A', 'B', 'C')
