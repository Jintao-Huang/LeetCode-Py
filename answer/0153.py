from leetcode_alg import *


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        def cond(mid: int) -> bool:
            return nums[mid] <= nums[n-1]
        idx = lower_bound(0, n-1, cond)
        return nums[idx]


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(Solution().findMin(nums))
