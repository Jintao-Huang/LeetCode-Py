from leetcode_alg import *


class Solution:
    """recommended"""

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        n = len(nums)
        for i, x in enumerate(nums[:n-2]):
            if x + nums[i+1] + nums[i+2] > 0:
                break
            if x + nums[n-2] + nums[n-1] < 0:
                continue
            #
            if i > 0 and nums[i-1] == x:
                continue
            lo, hi = i+1, n-1
            target = -x
            two_sum(nums, lo, hi, target, res, (x,))
        return res


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        cnt = Counter[int](nums)
        nums.sort()
        unique(nums)
        n = len(nums)
        for i, x in enumerate(nums):
            if x > 0:
                break
            if x + 2*nums[n-1] < 0:
                continue
            if cnt[x] >= 3 and x == 0:
                res.append([x, x, x])
            #
            for y in nums[i+1:n]:
                if cnt[x] >= 2 and 2*x+y == 0:
                    res.append([x, x, y])
                    continue
                if cnt[y] >= 2 and x+2*y == 0:
                    res.append([x, y, y])
                    continue
                #
                z = -x-y
                if z > y and z in cnt:
                    res.append([x, y, z])
        return res


if __name__ == "__main__":
    nums = [0, 0, 0]
    print(Solution().threeSum(nums))
    print(Solution2().threeSum(nums))
