# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from ..._types import *


def gcd(x: int, y: int) -> int:
    while y > 0:
        x, y = y, x % y
    return x


def lcm(x: int, y: int) -> int:
    return x * y // gcd(x, y)


def fast_pow(x: int, y: int, mod: int) -> int:
    """use pow(x, y, mod)"""
    res = 1
    while y > 0:
        if y % 2 == 0:
            y //= 2
            x *= x
            x %= mod
        else:
            y -= 1
            res *= x
            res %= mod
    return res
