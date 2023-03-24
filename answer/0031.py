
from leetcode_alg import *


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        next_permutation(nums)


if __name__ == "__main__":
    nums = [5, 1, 1]
    Solution().nextPermutation(nums)
    assert nums == [1, 1, 5]
