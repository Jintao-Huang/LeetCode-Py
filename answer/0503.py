from leetcode_alg import *


class Solution:
    """faster. 优化"""

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n):
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
            stack.append(i)

        for i in range(n):
            if len(stack) == 0:
                break
            while nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
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
