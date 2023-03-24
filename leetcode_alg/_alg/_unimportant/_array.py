# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from ..._types import *


def euclidean_dist(x: int, y: int, x2: int, y2: int, square: bool = False) -> float:
    # 使用math.dist
    d, d2 = x2 - x, y2 - y
    res = d*d + d2*d2
    if square:
        return res
    #
    res = sqrt(res)
    return res


def manhattan_dist(x: int, y: int, x2: int, y2: int) -> int:
    d, d2 = x2 - x, y2 - y
    return abs(d) + abs(d2)
