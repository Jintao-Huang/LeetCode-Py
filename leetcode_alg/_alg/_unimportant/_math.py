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
