from leetcode_alg import *


class Solution:
    """recommended"""

    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        mapper = discretize(nums)
        n = len(mapper)
        bit = BinaryIndexedTree([0] * n, False)
        for x0 in reversed(nums):
            x = mapper[x0]  # 0..n-1
            if x-1 >= 0:
                res += bit.prefix_sum(x-1)
            bit.add(x, 1)
        return res


class Solution2:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        mapper = discretize(nums)
        n = len(mapper)
        st = SegmentTree([0] * n, False)
        for x0 in nums:  # 也可以改成reversed的版本
            x = mapper[x0]  # 0..n-1
            if x+1 < n:
                res += st.query_range(x+1, n-1)
            st.update(x, 1)
        return res


class Solution3:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        mapper = discretize(nums)
        n = len(mapper)
        bit = BinaryIndexedTree2([0] * n, False)
        for x0 in reversed(nums):
            x = mapper[x0]  # 0..n-1
            if x-1 >= 0:
                res += bit.prefix_sum(x-1)
            bit.update_range(x, x, 1)
        return res


class Solution4:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        mapper = discretize(nums)
        n = len(mapper)
        st = SegmentTree2([0] * n, False)
        for x0 in nums:
            x = mapper[x0]  # 0..n-1
            if x+1 < n:
                res += st.query_range(x+1, n-1)
            st.update_range(x, x, 1)
        return res


class Solution5:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        sl = SortedList()
        for x0 in reversed(nums):
            res += sl.bisect_left(x0)
            sl.add(x0)
        return res
    
class Solution6:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        sl = SimpleSortedList()
        for x0 in reversed(nums):
            res += sl.bisect_left(x0)
            sl.add(x0)
        return res

class Solution7:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        sl = SimpleSortedList(key=neg)
        for x0 in nums: 
            res += sl.bisect_left(x0)
            sl.add(x0)
        return res

if __name__ == "__main__":
    nums = [7, 5, 6, 4]
    print(Solution().reversePairs(nums))
    print(Solution2().reversePairs(nums))
    print(Solution3().reversePairs(nums))
    print(Solution4().reversePairs(nums))
    print(Solution5().reversePairs(nums))
    print(Solution6().reversePairs(nums))
    print(Solution7().reversePairs(nums))
