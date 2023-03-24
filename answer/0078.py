
from leetcode_alg import *


class Solution:
    """回溯法"""

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return subsets2(nums)


class Solution2:
    """迭代法"""

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return subsets(nums)


class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(n + 1):
            ans += combinations(nums, i)
        return ans


if __name__ == "__main__":
    nums = [1, 2, 3]
    assert Solution().subsets(nums) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    assert Solution2().subsets(nums) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert Solution3().subsets(nums) == [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
