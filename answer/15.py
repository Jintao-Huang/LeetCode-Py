from leetcode_alg import *


class Solution:
    """recommended"""

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            x = nums[i]
            if x + nums[i+1]+nums[i+2] > 0:
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
        for i in range(n):
            x = nums[i]
            if x > 0:
                break
            if x + nums[n-1]*2 < 0:
                continue
            if cnt[x] >= 3 and x == 0:
                res.append([x, x, x])
            #
            for j in range(i+1, n):
                y = nums[j]
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
