from leetcode_alg import *


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            if nums[i] + nums[i+1]+nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
            #
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, n-2):
                if nums[i] + nums[j]+nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                #
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                lo, hi = j+1, n-1
                t = target-nums[i]-nums[j]
                two_sum(nums, lo, hi, t, res, (nums[i], nums[j]))
        return res


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution().fourSum(nums, target))
