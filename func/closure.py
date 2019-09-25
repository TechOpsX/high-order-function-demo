# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


# 创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count_beta():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))     # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


if __name__ == '__main__':
    f1, f2, f3 = count()
    print(f1())
    print(f2())
    print(f3())
