from leetcode_alg import *


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        #
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            x = nums[i]
            if x + nums[i+1]+nums[i+2] + nums[i+3] > target:
                break
            if x + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
            #
            if i > 0 and nums[i-1] == x:
                continue
            for j in range(i+1, n-2):
                y = nums[j]
                if x+y+nums[j+1] + nums[j+2] > target:
                    break
                if x+y+nums[n-2] + nums[n-1] < target:
                    continue
                #
                if j > i+1 and nums[j-1] == y:
                    continue
                lo, hi = j+1, n-1
                t = target-x-y
                two_sum(nums, lo, hi, t, res, (x, y))
        return res


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    assert Solution().fourSum(nums, target) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    #
    nums = [0, 0]
    target = 0
    assert Solution().fourSum(nums, target) == []
