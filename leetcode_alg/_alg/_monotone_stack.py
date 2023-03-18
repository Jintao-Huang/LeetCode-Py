# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *
"""
next_gt: 
    monotone_stack(is_next=True, mode="gt")
    monotone_stack2(is_next=True, mode="gt") (or)
next_ge, next_lt, next_le, prev_gt, ... 类似
# 
next_gt_prev_ge:
    monotone_stack3(next_mode="gt")
next_ge_prev_gt:
    monotone_stack3(next_mode="ge")  
next_lt_prev_le, next_le_prev_lt 类似
prev_gt_next_ge 即 next_ge_prev_gt
"""

_func_mapper = {
    "gt": gt,
    "ge": ge,
    "lt": lt,
    "le": le,
}


def monotone_stack(nums: List[int],
                   is_next: bool,
                   mode: Literal["gt", "ge", "lt", "le"]) -> List[int]:
    """弹出栈时修改res. faster. (ge: 递减栈)"""
    n = len(nums)
    res = [-1] * n
    stack = []
    _iter = range(n)
    _comp = _func_mapper[mode]
    if not is_next:
        _iter = reversed(_iter)
    for i in _iter:
        while stack and _comp(nums[i], nums[stack[-1]]):
            res[stack.pop()] = i
        stack.append(i)
    return res


def monotone_stack2(nums: List[int],
                    is_next: bool,
                    mode: Literal["gt", "ge", "lt", "le"]) -> List[int]:
    """monotone_stack的实现2. 加入栈时修改res (没有实用价值, slower, 为了让monotone_stack3更易理解)
    gt: 递减栈"""
    n = len(nums)
    res = [-1] * n
    stack = []
    _iter = range(n)
    _comp = _func_mapper[mode]
    if is_next:
        _iter = reversed(_iter)
    for i in _iter:
        while stack and not _comp(nums[stack[-1]], nums[i]):
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(i)
    return res


def monotone_stack3(nums: List[int],
                    next_mode: Literal["gt", "ge", "lt", "le"]) -> Tuple[List[int],  List[int]]:
    """将monotone_stack和monotone_stack2结合, 使得一次遍历解决两次遍历的问题. 
    note: ge(递减栈)/le (快)> gt/lt"""
    n = len(nums)
    res, res2 = [-1] * n, [-1] * n
    stack = []
    _comp = _func_mapper[next_mode]
    for i, x in enumerate(nums):
        while stack and _comp(x, nums[stack[-1]]):
            res[stack.pop()] = i
        if stack:
            res2[i] = stack[-1]
        stack.append(i)
    return res, res2


def largest_rect(nums: List[int]) -> int:
    """特例优化"""
    res = 0
    nums.append(0)  # 边界处理
    stack = [-1]  # nums[-1] == 0
    for i, x in enumerate(nums):
        # lo..idx..i
        while lt(x, nums[stack[-1]]):
            idx = stack.pop()
            lo = stack[-1]
            s = nums[idx] * (i - lo-1)  # h*w
            if s > res:
                res = s
        # 避免栈中出现重复的元素
        if x == nums[stack[-1]]:
            stack[-1] = i
        else:  # >
            stack.append(i)
    nums.pop()
    return res


def largest_rect2(nums: List[int]) -> int:
    """实现2, slower"""
    next_le, prev_lt = monotone_stack3(nums, "le")
    n = len(nums)
    res = 0
    # j..i..k
    for i in range(n):
        j = prev_lt[i]
        k = next_le[i]
        if j == -1:
            j = -1
        if k == -1:
            k = n
        s = nums[i] * (k - j - 1)  # h*w
        if s > res:
            res = s
    return res
