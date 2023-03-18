from leetcode_alg import *


class Solution:
    """faster. 优化. 单调栈"""

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i, x in enumerate(nums):
            while stack and x > nums[stack[-1]]:
                res[stack.pop()] = x
            stack.append(i)

        for i, x in enumerate(nums):
            if len(stack) == 0:
                break
            while x > nums[stack[-1]]:
                res[stack.pop()] = x
        return res


class Solution2:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums * 2
        ms = monotone_stack(nums, True, "gt")
        ms = [nums[i] if i != -1 else i for i in ms]
        return ms[:n]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 3]
    assert Solution().nextGreaterElements(nums) == [2, 3, 4, -1, 4]
    assert Solution2().nextGreaterElements(nums) == [2, 3, 4, -1, 4]
