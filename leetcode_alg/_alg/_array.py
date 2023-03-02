from typing import List

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
    """C0=A0, C1=A1-A0, ..."""
    if len(nums) == 0:
        return []
    res = [nums[0]]
    n = len(nums)
    for i in range(1, n):
        res.append(nums[i] - nums[i-1])
    return res