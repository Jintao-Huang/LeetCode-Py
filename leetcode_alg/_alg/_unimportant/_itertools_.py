# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

# 这里是itertools库中的等价实现. 实践中请使用itertools库.
# note: 接口略微不同(方便leetcode使用)

from ..._types import *
from .._array import reverse


def accumulate_(nums: List[int], func: Callable[[int, int], int] = add, *,
                initial: Optional[int] = None) -> List[int]:
    it = iter(nums)
    if initial is None:
        try:
            initial = next(it)
        except StopIteration:
            return []
    res = [initial]
    for x in it:
        res.append(func(res[-1], x))
    return res


def product_(*nums: List[int], repeat: int = 1) -> List[List[int]]:
    """nums: const"""
    t_list = [list(it) for it in nums] * repeat
    res = [[]]
    for t in t_list:
        res = [r + [x] for r in res for x in t]
    return res


def permutations_(nums: List[int], r: Optional[int] = None) -> List[List[int]]:
    res = []
    n = len(nums)
    if r is None:
        r = n
    if r > n:
        return res
    idxs = list(range(n))
    gt_idxs = list(range(1, r+1))
    res.append([nums[i] for i in idxs[:r]])
    while True:
        i = r-1
        while i >= 0:
            if gt_idxs[i] >= n:
                gt_idxs[i] = i+1
            else:
                reverse(idxs, i+1, n-1)
                j = gt_idxs[i]
                idxs[i], idxs[j] = idxs[j], idxs[i]
                res.append([nums[i] for i in idxs[:r]])
                gt_idxs[i] += 1
                break
            i -= 1
        else:
            break
    return res


def _dfs_p(nums: List[int], r: int, visited: List[bool],
           path: List[int], res: List[List[int]]) -> None:
    """perm, comb, comb_wr, subset区别:  
    perm: visited, 没有idx
    comb: break优化, i+1
    comb_wr: i
    subset: 无需要判断条件(res.append), i+1
    相同点: for循环
    """
    if r == 0:
        res.append(path[:])
        return

    for i, x in enumerate(nums):
        if visited[i]:
            continue
        #
        path.append(x)
        visited[i] = True
        _dfs_p(nums, r-1, visited, path, res)
        path.pop()
        visited[i] = False


def permutations2(nums: List[int], r: Optional[int] = None) -> List[List[int]]:
    n = len(nums)
    if r is None:
        r = n
    visited = [False] * n
    res = []
    _dfs_p(nums, r, visited, [], res)
    return res


def combinations_(nums: List[int], r: int) -> List[List[int]]:
    """nums: const"""
    n = len(nums)
    res: List[List[int]] = []
    if r > n:
        return res
    #
    idxs = list(range(r))
    res.append([nums[i] for i in idxs])
    while True:
        # 从后往前找未到达最大的数. e.g. idxs=[0,1,3], n=4, 则i=1处为非最大数.
        i = r-1
        while i >= 0 and idxs[i] == n-r+i:
            i -= 1
        if i < 0:
            break
        # 修改的后面的数, 依次递增. e.g. [1,2,6,7]. 该idx[1]+=1, 则->[1,3,4,5]
        idxs[i] += 1
        idxs[i+1:] = range(idxs[i]+1, idxs[i]+r-i)
        res.append([nums[i] for i in idxs])
    return res


def _dfs_c(nums: List[int], r: int, idx: int, path: List[int], res: List[List[int]]) -> None:
    if r == 0:
        res.append([nums[i] for i in path])
        return
    n = len(nums)
    #
    for i in range(idx, n):
        if n - i < r:
            break
        path.append(i)
        _dfs_c(nums, r-1, i+1, path, res)
        path.pop()


def combinations2(nums: List[int], r: int) -> List[List[int]]:
    """nums: const"""
    res = []
    _dfs_c(nums, r, 0, [], res)
    return res


def combinations_with_replacement_(nums: List[int], r: int) -> List[List[int]]:
    """nums: const"""
    n = len(nums)
    res: List[List[int]] = []
    if r > n:
        return res
    #
    idxs = [0] * r
    res.append([nums[i] for i in idxs])
    while True:
        # 从后往前找未到达最大的数. e.g. idxs=[0,2,3], n=4, 则i=1处为非最大数
        i = r-1
        while i >= 0 and idxs[i] == n-1:
            i -= 1
        if i < 0:
            break
        # 修改的后面的数. e.g. [1,2,6,7]. 该idx[1]+=1, 则->[1,3,3,3]
        idxs[i:] = [idxs[i]+1] * (r-i)
        res.append([nums[i] for i in idxs])
    return res


def _dfs_cwr(nums: List[int], r: int, idx: int, path: List[int], res: List[List[int]]) -> None:
    if r == 0:
        res.append([nums[i] for i in path])
        return
    n = len(nums)
    #
    for i in range(idx, n):
        path.append(i)
        _dfs_cwr(nums, r-1, i, path, res)
        path.pop()


def combinations_with_replacement2(nums: List[int], r: int) -> List[List[int]]:
    """nums: const"""
    res = []
    _dfs_cwr(nums, r, 0, [], res)
    return res
