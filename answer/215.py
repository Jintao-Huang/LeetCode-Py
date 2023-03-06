from leetcode_alg import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return find_kth_smallest(nums, n-k)


class Solution2:
    """recommended"""

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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return sorted(nums)[n-k]


class Solution4:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = heapq.nlargest(k, nums)
        return res[-1]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(Solution().findKthLargest(nums, k))
    print(Solution2().findKthLargest(nums, k))
    print(Solution3().findKthLargest(nums, k))
    print(Solution4().findKthLargest(nums, k))
