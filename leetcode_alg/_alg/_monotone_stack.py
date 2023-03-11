# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *
"""
next_gt: 
    monotone_stack(is_prev=False, mode="gt")
    monotone_stack2(is_next=True, mode="gt") (or)
next_ge, next_lt, next_le, prev_gt, ... 类似
"""
_func_mapper = {
    "gt": gt,
    "ge": ge,
    "lt": lt,
    "le": le,
}


def monotone_stack(nums: List[int],
                   is_prev: bool,
                   mode: Literal["gt", "ge", "lt", "le"]) -> List[int]:
    """弹出栈时, 修改res. faster"""
    n = len(nums)
    res = [-1] * n
    stack = []
    _iter = range(n)
    comp = _func_mapper[mode]
    if is_prev:
        _iter = reversed(_iter)
    for i in _iter:
        x = nums[i]
        while len(stack) > 0 and comp(x, nums[stack[-1]]):
            res[stack.pop()] = i
        stack.append(i)
    return res


def monotone_stack2(nums: List[int],
                    is_next: bool,
                    mode: Literal["gt", "ge", "lt", "le"]) -> List[int]:
    """实现2: 加入栈时, 修改res. (没有实用价值, slower)"""
    n = len(nums)
    res = [-1] * n
    stack = []
    _iter = range(n)
    comp = _func_mapper[mode]
    if is_next:
        _iter = reversed(_iter)
    for i in _iter:
        x = nums[i]
        while len(stack) > 0 and not comp(nums[stack[-1]], x):
            stack.pop()
        if len(stack) > 0:
            res[i] = stack[-1]
        stack.append(i)
    return res
