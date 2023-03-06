
from leetcode_alg import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper: Dict[int, int] = {}
        for i, x in enumerate(nums):
            tsx = target - x  # target sub x
            if tsx in mapper:
                return [mapper[tsx], i]
            mapper[x] = i
        # 
        return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))  # [0,1]