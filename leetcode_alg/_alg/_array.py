from .._types import *


def unique(nums: List[int]) -> None:
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
    """C0=A0, C1=A1-A0, ...
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
    """it1: str, bytes, bytearray, list"""
    res = 0
    for c, c2 in zip(it1, it2):
        if c != c2:
            break
        res += 1
    return res
