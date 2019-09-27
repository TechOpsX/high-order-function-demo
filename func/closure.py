# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            # print(hex(id(i)))
            return i*i
        fs.append(f)
    return fs


# 创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count_beta():
    def f(j):
        # print(hex(id(j)))

        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))     # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


# 练习 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def create_counter():
    i = 0

    def counter():
        nonlocal i
        i = i + 1
        return i

    return counter


# Todo，实现一个不用global的函数级别计数器
def f():
    def x():
        if not hasattr(f, 'x'):
            f.x = 0
        f.x = f.x + 1
        return f.x
    return x


if __name__ == '__main__':
    f1, f2, f3 = count()
    print(f1())
    print(f2())
    print(f3())
    counterA = create_counter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = create_counter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')
