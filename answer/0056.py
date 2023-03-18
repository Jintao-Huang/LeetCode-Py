
from leetcode_alg import *


class Solution:
    """recommended. 贪心"""
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=itemgetter(0))
        return merge_intervals(intervals)


class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=itemgetter(1))
        return merge_intervals2(intervals)


if __name__ == "__main__":
    intervals = [[1, 3], [8, 10], [15, 18], [2, 6]]
    assert Solution().merge(intervals) == [[1, 6], [8, 10], [15, 18]]
    intervals = [[1, 3], [8, 10], [15, 18], [2, 6]]
    assert Solution2().merge(intervals) == [[1, 6], [8, 10], [15, 18]]
