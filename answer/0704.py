
from leetcode_alg import *
from leetcode_alg.ext import binary_search


class Solution:
    """faster"""

    def search(self, nums: List[int], target: int) -> int:
        idx = bisect_left(nums, target)
        if idx >= len(nums) or nums[idx] != target:
            idx = -1
        return idx


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target)


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    print(Solution().search(nums, 13))
    print(Solution2().search(nums, 13))
