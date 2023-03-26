from leetcode_alg import *


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        #
        res = knapsack(nums, s // 2, True, "max", True, -1)
        return False if res == -1 else True


def knapsack_new(choices: List[int], capacity: int) -> bool:
    dp = [-1] * (capacity+1)
    dp[0] = 0
    #
    for c in choices:
        for capa in reversed(range(c, capacity+1)):
            c2 = capa-c
            if dp[c2] != -1 and (dp[c2]+1) > dp[capa]:
                dp[capa] = dp[c2] + 1
        if dp[capacity] > 0:
            return True  # 及时返回
    return False


class Solution2:
    """针对问题的优化. 背包"""

    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        #
        return knapsack_new(nums, s // 2)


class Solution3:
    """recommended. 哈希表"""

    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        #
        target = s // 2
        _set = {0}
        for i in nums:
            if target-i in _set:
                return True
            for x in list(_set):
                _set.add(x+i)
        return False


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    assert Solution().canPartition(nums) is True
    assert Solution2().canPartition(nums) is True
    assert Solution3().canPartition(nums) is True
