# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from ..._types import *
from .._array import merge, partition
from ..._ds._heap import *


def quick_sort(nums: List[int], lo: int, hi: int) -> None:
    """[lo..hi]"""
    if lo >= hi:
        return
    rand_int = randint(lo, hi)  # [lo..hi]
    nums[lo], nums[rand_int] = nums[rand_int], nums[lo]
    pivot = partition(nums, lo, hi)
    quick_sort(nums, lo, pivot - 1)
    quick_sort(nums, pivot+1, hi)


def merge_sort(nums: List[int], lo: int, hi: int) -> None:
    """[lo..hi]"""
    if lo == hi:
        return
    mid = (lo + hi) >> 1
    merge_sort(nums, lo, mid)
    merge_sort(nums, mid+1, hi)
    merge(nums, lo, mid, hi)


def _siftdown_max(heap: List[int], i: int, hi: int) -> None:
    """下滤. 增加了hi参数[0..i..hi]"""
    x0 = heap[i]
    while (ci:=(i<<1)+1)<= hi:
        if ci+1 <= hi and heap[ci+1] > heap[ci]:
            ci += 1
        cx = heap[ci]
        if not cx > x0:
            break
        heap[i] = cx
        i = ci
    heap[i] = x0


def heap_sort(nums: List[int]) -> None:
    """inplace"""
    n = len(nums)
    if n == 0:
        return
    heapify_max(nums)  # C
    nums[0], nums[n-1] = nums[n-1], nums[0]
    for hi in reversed(range(1, n-1)):
        _siftdown_max(nums, 0, hi)  # py
        nums[0], nums[hi] = nums[hi], nums[0]


def heap_sort2(nums: List[int]) -> List[int]:
    """nums: not const. 用python的heapq库(C)"""
    res = []
    n = len(nums)
    heapify(nums)
    for _ in range(n):
        res.append(heappop(nums))
    return res
