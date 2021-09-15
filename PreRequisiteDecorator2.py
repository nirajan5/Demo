def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result

x = operate(inc, 10)
y = operate(dec, 10)
print(x)
print(y)
