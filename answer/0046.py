
from leetcode_alg import *
from leetcode_alg.ext import permutations_, permutations2


class Solution:
    """faster"""

    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))   # leetcode不检查list和tuple.


class Solution2:
    """回溯法"""

    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations2(nums)


class Solution3:
    """迭代法"""

    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations_(nums)


if __name__ == "__main__":
    nums = [1, 2, 3]
    assert Solution().permute(nums) == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    assert Solution2().permute(nums) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert Solution3().permute(nums) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
