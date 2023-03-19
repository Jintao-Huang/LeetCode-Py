
from leetcode_alg import *


class Solution:
    """贪心"""

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        end = -INF
        intervals.sort(key=itemgetter(1))  # 为后面保留更多的空间
        for itv in intervals:
            if end <= itv[0]:
                res += 1
                end = itv[1]
        return len(intervals)-res


class Solution2:
    """DP. 超时"""

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=itemgetter(0))
        n = len(intervals)
        dp = [1] * n
        for i, itv in enumerate(intervals):
            for j in range(i):
                itv2 = intervals[j]
                if itv2[1] <= itv[0] and (dp[j] + 1) > dp[i]:
                    dp[i] = dp[j] + 1
        return n-dp[n-1]


class Solution3:
    """LIS改造"""

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=itemgetter(0))
        n = len(intervals)
        stack = []
        for s, e in intervals:
            idx = bisect_left(stack, s+1)
            if idx >= len(stack):
                stack.append(e)
            elif e < stack[idx]:
                stack[idx] = e
        return n-len(stack)


if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    assert Solution().eraseOverlapIntervals(intervals) == 1
    assert Solution2().eraseOverlapIntervals(intervals) == 1
    assert Solution3().eraseOverlapIntervals(intervals) == 1
