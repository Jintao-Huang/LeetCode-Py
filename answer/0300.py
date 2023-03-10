from leetcode_alg import *


class Solution:
    """recommended"""
    def lengthOfLIS(self, nums: List[int]) -> int:
        return LIS(nums)


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return LIS2(nums)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    assert Solution().lengthOfLIS(nums) == 4
    assert Solution2().lengthOfLIS(nums) == 4
