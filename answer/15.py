from leetcode_alg import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if nums[i] + nums[i+1]+nums[i+2] > 0:
                break
            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue
            #
            if i > 0 and nums[i-1] == nums[i]:
                continue
            lo, hi = i+1, n-1
            target = -nums[i]
            two_sum(nums, lo, hi, target, res, (nums[i],))
        return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
