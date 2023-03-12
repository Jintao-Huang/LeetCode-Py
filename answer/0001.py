
from leetcode_alg import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper: Dict[int, int] = {}
        for i, x in enumerate(nums):
            tmx = target - x  # target minus x
            if tmx in mapper:
                return [mapper[tmx], i]
            mapper[x] = i
        #
        return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    assert Solution().twoSum(nums, target) == [0, 1]
