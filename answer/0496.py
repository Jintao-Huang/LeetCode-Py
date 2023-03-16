from leetcode_alg import *


class Solution:
    """faster"""

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stack = []
        mapper = {}
        # 存数值, 而不是索引
        for i in range(n):
            x = nums2[i]
            while len(stack) > 0 and gt(x, stack[-1]):
                mapper[stack.pop()] = x
            stack.append(x)
        #
        res = []
        for x in nums1:
            res.append(mapper.get(x, -1))
        return res


class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ms = monotone_stack(nums2, True, "gt")
        mapper = {}
        for i, x in zip(ms, nums2):
            mapper[x] = nums2[i] if i != -1 else -1
        res = []
        for x in nums1:
            res.append(mapper[x])
        return res


class Solution3:
    """模板2"""

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ms = monotone_stack2(nums2, True, "gt")
        mapper = {}
        for i, x in zip(ms, nums2):
            mapper[x] = nums2[i] if i != -1 else -1
        res = []
        for x in nums1:
            res.append(mapper[x])
        return res


if __name__ == "__main__":
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    assert Solution().nextGreaterElement(nums1, nums2) == [-1, 3, -1]
    assert Solution2().nextGreaterElement(nums1, nums2) == [-1, 3, -1]
    assert Solution3().nextGreaterElement(nums1, nums2) == [-1, 3, -1]
