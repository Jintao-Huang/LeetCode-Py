# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *

_func_mapper = {
    "max": ge,
    "min": le,
}


def monotone_deque(nums: List[int], k: int, is_next: bool,
                   mode: Literal["max", "min"]) -> List[int]:
    """最近k个(含自己)的最大/最小
    return: [N]
    """
    _comp = _func_mapper[mode]
    dq = Deque[int]()
    n = len(nums)
    res = [-1] * n
    _iter = range(n)
    if is_next:
        _iter = reversed(_iter)
    #
    for i in _iter:
        while dq and _comp(nums[i], nums[dq[-1]]):
            dq.pop()
        dq.append(i)
        if abs(i - dq[0]) >= k:
            dq.popleft()
        res[i] = nums[dq[0]]
    return res
