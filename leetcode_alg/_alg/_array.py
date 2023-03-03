# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *


def unique(nums: List[int]) -> None:
    """nums已有序: inplace"""
    n = len(nums)
    lo = 1  # 将被赋值, 但未被赋值. ignore 0
    for hi in range(1, n):
        if nums[hi] != nums[hi-1]:
            nums[lo] = nums[hi]
            lo += 1
    #
    for _ in range(lo, n):
        nums.pop()


def diff(nums: List[int]) -> List[int]:
    """res[0]=nums[0], res[1]=nums[1]-nums[0], res[2]=nums[2]-nums[1]
    nums: const
    """
    n = len(nums)
    if n == 0:
        return []
    res = [nums[0]]
    for i in range(1, n):
        res.append(nums[i] - nums[i-1])
    return res


def find_prefix(it1: Iterable, it2: Iterable) -> int:
    """it1: str, bytes, bytearray, list. 返回相同前缀的索引"""
    res = 0
    for c, c2 in zip(it1, it2):
        if c != c2:
            break
        res += 1
    return res


def euclidean_dist(x1: int, y1: int, x2: int, y2: int,
                   square: bool = False) -> float:
    d1, d2 = x2 - x1, y2 - y1
    res = d1*d1 + d2*d2
    if square:
        return res
    #
    res = sqrt(res)
    return res


def manhattan_dist(x1: int, y1: int, x2: int, y2: int) -> float:
    d1, d2 = x2 - x1, y2 - y1
    return abs(d1) + abs(d2)


def partition(nums: List[int], lo: int, hi: int) -> int:
    """将nums[lo]作为pivot. 将nums中<pivot放其左边, >pivot放其右边(==pivot随意)
    (算法逻辑更简单). ref: 算法导论"""
    nums[lo], nums[hi] = nums[hi], nums[lo]
    pivot = nums[hi]
    for i in range(lo, hi):
        if nums[i] <= pivot:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
    nums[lo], nums[hi] = nums[hi], nums[lo]
    return lo


def partition2(nums: List[int], lo: int, hi: int) -> int:
    assert 0 <= lo <= hi < len(nums)
    pivot = nums[lo]
    while lo < hi:
        while True:
            if nums[hi] < pivot:
                nums[lo] = nums[hi]
                lo += 1
                break
            hi -= 1
            if lo == hi:  # do while
                break
        while lo < hi:
            if nums[lo] > pivot:
                nums[hi] = nums[lo]
                hi -= 1
                break
            lo += 1
    nums[lo] = pivot
    return lo


def merge(nums: List[int], lo: int, mid: int, hi: int, inf: int = int(1e9)) -> None:
    """nums: [lo..mid], [mid+1..hi], 分别有序, 合并成一个有序的nums. (inplace)
    (算法逻辑更简单). ref: 算法导论"""
    assert 0 <= lo <= mid < hi < len(nums)
    A = nums[lo:mid+1].copy()
    B = nums[mid+1:hi+1].copy()
    A.append(inf)
    B.append(inf)
    i, j = 0, 0
    for k in range(lo, hi+1):
        if A[i] <= B[j]:
            nums[k] = A[i]
            i += 1
        else:
            nums[k] = B[j]
            j += 1


def merge2(nums: List[int], lo: int, mid: int, hi: int) -> None:
    assert 0 <= lo <= mid < hi < len(nums)
    helper = nums[lo:mid+1].copy()
    msl = mid-lo  # mid sub lo
    i, j, k = mid+1, 0, lo
    while i <= hi and j <= msl:
        if nums[i] <= helper[j]:
            nums[k] = nums[i]
            i += 1
        else:
            nums[k] = helper[j]
            j += 1
        k += 1
    #
    while j <= msl:
        nums[k] = helper[j]
        j += 1
        k += 1


def find_kth_smallest(nums: List[int], k: int) -> int:
    """nums无序, 查找第k小的数(即sort后索引是k, 从0数). 平均复杂度O(n)"""
    lo, hi = 0, len(nums) - 1
    assert lo <= k <= hi
    while True:
        rand_idx = randint(lo, hi)  # [lo..hi]
        nums[lo], nums[rand_idx] = nums[rand_idx], nums[lo]
        pivot = partition(nums, lo, hi)
        if pivot == k:
            return nums[pivot]
        elif pivot < k:
            lo = pivot + 1
        else:
            hi = pivot - 1


def prefix_sum(nums: List[int], res: List[int]) -> None:
    """前缀和. 若输入时, len(res)==0, res[0]=nums[0], res[1]=nums[0]+nums[1], res[2]=sum(nums[0..2])"""
    n = len(nums)
    if n == 0:
        return
    _start = 0
    if len(res) == 0:
        res.append(nums[0])
        _start = 1
    for i in range(_start, n):
        res.append(res[-1]+nums[i])
