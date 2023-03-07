from leetcode_alg import *


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        #
        res = []
        nums.sort()
        n = len(nums)
        for i, x in enumerate(nums[:n-3]):
            if x + nums[i+1]+nums[i+2] + nums[i+3] > target:
                break
            if x + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
            #
            if i > 0 and nums[i-1] == x:
                continue
            for j, y in enumerate(nums[i+1:n-2], i+1):
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
    # nums = [1, 0, -1, 0, -2, 2]
    # target = 0
    # print(Solution().fourSum(nums, target))
    #
    nums = [0, 0]
    target = 0
    print(Solution().fourSum(nums, target))