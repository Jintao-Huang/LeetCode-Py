from leetcode_alg import *


class Solution:
    """recommended. 贪心. """

    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        idx = bisect_left(intervals, newInterval)
        res = intervals[:idx]
        #
        if len(res) == 0 or newInterval[0] > res[-1][1]:
            res.append(newInterval)
        elif res[-1][1] < newInterval[1]:
            res[-1][1] = newInterval[1]
        #
        n = len(intervals)
        while idx < n:
            itv = intervals[idx]
            if itv[0] > res[-1][1]:
                break
            if res[-1][1] < itv[1]:
                res[-1][1] = itv[1]
            idx += 1
        #
        res += intervals[idx:]
        return res


class Solution2:
    """faster than 3"""

    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        idx = bisect_left(intervals, newInterval)  # C
        intervals.insert(idx, newInterval)
        return merge_intervals(intervals)


class Solution3:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        idx = lower_bound(0, len(intervals), lambda mid: intervals[mid][0] >= newInterval[0])
        intervals.insert(idx, newInterval)
        return merge_intervals(intervals)


if __name__ == "__main__":
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    assert Solution().insert(intervals, newInterval) == [[1, 5], [6, 9]]
    assert Solution2().insert(intervals, newInterval) == [[1, 5], [6, 9]]
    assert Solution3().insert(intervals, newInterval) == [[1, 5], [6, 9]]
