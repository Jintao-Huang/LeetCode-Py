# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from ..._types import *
from .._search import lower_bound


def bisect_left(nums: List[int], x: int, lo: int = 0, hi: Optional[int] = None) -> int:
    """[lo..hi)"""
    n = len(nums)
    if hi is None:
        hi = len(nums)
    assert 0 <= lo < hi <= n
    return lower_bound(lo, hi, lambda mid: nums[mid] >= x)


def bisect_right(nums: List[int], x: int, lo: int = 0, hi: Optional[int] = None) -> int:
    """[lo..hi)"""
    n = len(nums)
    if hi is None:
        hi = len(nums)
    assert 0 <= lo < hi <= n
    return lower_bound(lo, hi, lambda mid: nums[mid] > x)


def binary_search(nums: List[int], x: int, lo: int = 0, hi: Optional[int] = None) -> int:
    """[lo..hi). 返回的索引是[0..hi-1], 或-1(未找到). 若nums中存在多个x, 则返回任意一个x的索引"""
    n = len(nums)
    if hi is None:
        hi = n
    assert 0 <= lo < hi <= n
    # 
    hi -= 1
    while lo <= hi:
        mid = (lo+hi) >> 1
        if nums[mid] == x:
            return mid
        elif nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
