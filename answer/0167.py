from leetcode_alg import *


class Solution:
    """双指针"""
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers)-1
        while lo < hi:
            x = numbers[lo]+numbers[hi]
            if x == target:
                return [lo + 1, hi + 1]
            elif x < target:
                lo += 1
            else:
                hi -= 1
        return []


class Solution2:
    """faster. 哈希表"""

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapper: Dict[int, int] = {}
        for i, x in enumerate(numbers):
            tmx = target - x  # target minus x
            if tmx in mapper:
                return [mapper[tmx]+1, i+1]
            mapper[x] = i
        #
        return []


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    assert Solution().twoSum(numbers, target) == [1, 2]
    assert Solution2().twoSum(numbers, target) == [1, 2]
