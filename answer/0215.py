from leetcode_alg import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return quick_select(nums, n-k)


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n-k+1 <= k:
            heap = Heap(nums)
            for _ in range(n-k+1):
                res = heap.pop()
        else:
            heap = Heap(nums, max_heap=True)
            for _ in range(k):
                res = heap.pop()
        return res


class Solution3:
    """自己实现nlargest"""

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n-k+1 <= k:
            res = nsmallest_(nums, n-k+1)
            res.sort()
        else:
            res = nlargest_(nums, k)
            res.sort(reverse=True)
        return res[-1]


class Solution4:
    """桶排序. faster"""

    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val, max_val = min(nums), max(nums)
        n = max_val - min_val + 1
        bucket = [0] * n
        for x in nums:
            bucket[x-min_val] += 1
        #
        res = 0
        for i in reversed(range(n)):
            x = bucket[i]
            res += x
            if res >= k:
                return i + min_val


class Solution5:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n-k+1 <= k:
            res = nsmallest(n-k+1, nums)  # py
        else:
            res = nlargest(k, nums)
        return res[-1]


class Solution6:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return sorted(nums)[n-k]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert Solution().findKthLargest(nums, k) == 5
    assert Solution2().findKthLargest(nums[:], k) == 5
    assert Solution3().findKthLargest(nums[:], k) == 5
    assert Solution4().findKthLargest(nums[:], k) == 5
    assert Solution5().findKthLargest(nums[:], k) == 5
    assert Solution6().findKthLargest(nums, k) == 5
