from leetcode_alg import *


class Solution:
    """双指针"""
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = INF
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            x = nums[i]
            min_x = x + nums[i+1] + nums[i+2]
            if min_x >= target and abs(min_x - target) < abs(res - target):
                res = min_x
                break
            max_x = x + nums[n-2] + nums[n-1]
            if max_x <= target and abs(max_x - target) < abs(res - target):
                res = max_x
                continue
            #
            if i > 0 and nums[i-1] == x:
                continue
            lo, hi = i+1, n-1
            while lo < hi:
                # if lo > i+1 and nums[lo-1] == nums[lo]:
                #     lo += 1
                #     continue
                # if hi < n-1 and nums[hi+1] == nums[hi]:
                #     hi -= 1
                #     continue
                z = x + nums[lo] + nums[hi]
                if z == target:
                    return z
                #
                if z < target:
                    lo += 1
                else:
                    hi -= 1
                if abs(z - target) < abs(res - target):
                    res = z
        return res


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    assert Solution().threeSumClosest(nums, target) == 2
