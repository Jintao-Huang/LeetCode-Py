# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from ..._types import *

def randperm(nums: List[int]) -> None:
    """ref: 算法导论"""
    n = len(nums)
    for i in range(n):
        idx = randint(i, n-1)  # [i..n-1]
        nums[i], nums[idx] = nums[idx], nums[i]
