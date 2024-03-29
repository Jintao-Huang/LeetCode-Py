from leetcode_alg import *


class Solution:
    """哈希表"""
    def fourSumCount(self, nums1: List[int], nums2: List[int],
                     nums3: List[int], nums4: List[int]) -> int:
        mapper = DefaultDict[int, int](int)
        for x in nums1:
            for y in nums2:
                mapper[x+y] += 1
        #
        res = 0
        for x in nums3:
            for y in nums4:
                res += mapper[-x-y]
        return res


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    assert Solution().fourSumCount(nums1, nums2, nums3, nums4) == 2
