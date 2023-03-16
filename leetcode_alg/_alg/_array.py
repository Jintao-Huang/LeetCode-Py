# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *


def unique(nums: List[int]) -> None:
    """nums已有序: inplace"""
    n = len(nums)
    lo = 1  # 将被赋值, 但未被赋值. ignore 0
    for hi in range(1, n):
        x = nums[hi]
        if x != nums[hi-1]:
            nums[lo] = x
            lo += 1
    #
    for _ in range(lo, n):
        nums.pop()


def diff(nums: List[int], initial: Optional[int] = None) -> List[int]:
    """res[0]=nums[0], res[1]=nums[1]-nums[0], res[2]=nums[2]-nums[1]
    nums: const
    """
    res = []
    if initial is not None:
        res.append(initial)
    #
    n = len(nums)
    if n == 0:
        return res
    if len(res) == 1:
        res.append(nums[0] - res[0])
    else:
        res.append(nums[0])
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


def partition(nums: List[int], lo: int, hi: int) -> int:
    """将nums[lo]作为pivot. 将nums中<pivot放其左边, >pivot放其右边(==pivot放其右边)
    (算法逻辑更简单). ref: 算法导论"""
    nums[lo], nums[hi] = nums[hi], nums[lo]
    pivot = nums[hi]
    for i in range(lo, hi):
        if nums[i] < pivot:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
    nums[lo], nums[hi] = nums[hi], nums[lo]
    return lo


def partition2(nums: List[int], lo: int, hi: int) -> int:
    """[lo..hi]. (==pivot随意)"""
    pivot = nums[lo]
    while lo < hi:
        while lo < hi and pivot <= nums[hi]:
            hi -= 1
        if lo < hi:
            nums[lo] = nums[hi]
            lo += 1
        while lo < hi and nums[lo] <= pivot:
            lo += 1
        if lo < hi:
            nums[hi] = nums[lo]
            hi -= 1
    nums[lo] = pivot
    return lo


def merge(nums: List[int], lo: int, mid: int, hi: int) -> None:
    """nums: [lo..mid], [mid+1..hi], 分别有序, 合并成一个有序的nums. (inplace)
    (算法逻辑更简单). ref: 算法导论"""
    A = nums[lo:mid+1]  # 浅copy
    B = nums[mid+1:hi+1]
    A.append(INF)
    B.append(INF)
    i, j = 0, 0
    for k in range(lo, hi+1):
        if A[i] <= B[j]:
            nums[k] = A[i]
            i += 1
        else:
            nums[k] = B[j]
            j += 1


def merge2(nums: List[int], lo: int, mid: int, hi: int) -> None:
    """[lo..mid], [mid+1,hi]"""
    helper = nums[lo:mid+1]
    mml = mid-lo  # mid minus lo
    i, j, k = mid+1, 0, lo
    while i <= hi and j <= mml:
        if nums[i] <= helper[j]:
            nums[k] = nums[i]
            i += 1
        else:
            nums[k] = helper[j]
            j += 1
        k += 1
    #
    while j <= mml:
        nums[k] = helper[j]
        j += 1
        k += 1


def quick_select(nums: List[int], k: int) -> int:
    """nums无序, 查找第k小的数(即sort后索引是k, 从0数). 平均复杂度O(n)"""
    lo, hi = 0, len(nums) - 1
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


def two_sum(nums: List[int], lo: int, hi: int, target: int, res: List[List[int]],
            res_prefix: Tuple[int, ...]):
    while lo < hi:
        x = nums[lo] + nums[hi]
        if x == target:
            res.append([*res_prefix, nums[lo], nums[hi]])
            lo += 1
            hi -= 1
            while lo < hi and nums[lo-1] == nums[lo]:
                lo += 1
            while lo < hi and nums[hi+1] == nums[hi]:
                hi -= 1
        elif x < target:
            lo += 1
        else:
            hi -= 1
