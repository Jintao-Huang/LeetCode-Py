
from leetcode_alg import *


class Solution:
    """faster, 优化. 单调队列"""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = Deque[int]()
        #
        for i in range(k):
            while dq and ge(nums[i], nums[dq[-1]]):
                dq.pop()
            dq.append(i)
        #
        res = [nums[dq[0]]]
        n = len(nums)
        for i in range(k, n):
            while dq and ge(nums[i], nums[dq[-1]]):
                dq.pop()
            dq.append(i)
            if i - dq[0] >= k:
                dq.popleft()
            res.append(nums[dq[0]])
        return res


class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return monotone_deque(nums, k, False, "max")[k-1:]


if __name__ == "__main__":
    nums = [7, 2, 4]
    assert Solution().maxSlidingWindow(nums, 2) == [7, 4]
    assert Solution2().maxSlidingWindow(nums, 2) == [7, 4]
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    assert Solution().maxSlidingWindow(nums, 3) == [3, 3, 5, 5, 6, 7]
    assert Solution2().maxSlidingWindow(nums, 3) == [3, 3, 5, 5, 6, 7]
