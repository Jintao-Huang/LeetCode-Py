# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from ..._types import *
from .._array import merge, partition


def merge_sort(nums: List[int], lo: int, hi: int) -> None:
    """[lo..hi]"""
    if lo == hi:
        return
    mid = (lo + hi) >> 1
    merge_sort(nums, lo, mid)
    merge_sort(nums, mid+1, hi)
    merge(nums, lo, mid, hi)


def quick_sort(nums: List[int], lo: int, hi: int) -> None:
    """[lo..hi]"""
    if lo >= hi:
        return
    rand_int = randint(lo, hi)  # [lo..hi]
    nums[lo], nums[rand_int] = nums[rand_int], nums[lo]
    pivot = partition(nums, lo, hi)
    quick_sort(nums, lo, pivot - 1)
    quick_sort(nums, pivot+1, hi)
