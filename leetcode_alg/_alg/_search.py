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


def _n_queens(path: List[int], res: List[List[int]],
              v: bytearray, v2: bytearray, v3: bytearray) -> None:
    """
    v: visited数组, 竖线. v2: 斜向下线, v3: 斜向上线
    """
    idx, n = len(path), len(v)
    if idx == n:
        res.append(path[:])
        return

    for i in range(n):
        if v[i] or v2[i-idx+n-1] or v3[idx+i]:
            continue
        v[i], v2[i-idx+n-1], v3[idx+i] = True, True, True
        path.append(i)
        _n_queens(path, res, v, v2, v3)
        v[i], v2[i-idx+n-1], v3[idx+i] = False, False, False
        path.pop()


def n_queens(n: int) -> List[List[int]]:
    v = bytearray(n)
    v2 = bytearray((n << 1)-1)
    v3 = bytearray((n << 1)-1)
    res: List[List[int]] = []
    _n_queens([], res, v, v2, v3)
    return res
