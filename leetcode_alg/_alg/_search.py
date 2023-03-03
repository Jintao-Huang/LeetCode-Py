# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *


def lower_bound(lo: int, hi: int, cond: Callable[[int], bool]) -> int:
    while lo < hi:
        mid = (lo + hi) >> 1  # 若是c++, 请改成lo+(hi-lo)>>1
        if cond(mid):
            hi = mid
        else:
            lo = mid+1
    return lo


def upper_bound(lo: int, hi: int, cond: Callable[[int], bool]) -> int:
    while lo < hi:
        mid = (lo + hi + 1) >> 1  # lo + (hi-lo+1)>>1
        if cond(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo
