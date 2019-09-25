"""
    map(f, [x1, x2, x3 ,x4])
    the same as
    for n in [x1, x2, x3,x4]:
        L.append(f(n))

    reduce(f, [x1, x2, x3 ,x4])
    the same as
    f(f(f(x1, x2), x3), x4)
"""
from functools import reduce


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


# demo str2int
def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# Write a str2float function using map and reduce
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}


def str2float(s):
    nums = map(lambda x: CHAR_TO_FLOAT[x], s)
    print(nums)
    point = 0

    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)


if __name__ == "__main__":
    print(str2float('0'))
    print(str2float('123.456'))
    print(str2float('123.45600'))
    print(str2float('0.1234'))
    print(str2float('.1234'))
    print(str2float('120.0034'))
