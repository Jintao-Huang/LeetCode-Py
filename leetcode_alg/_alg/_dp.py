# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *


def LIS(nums: List[int]) -> int:
    """O(nlogn)"""
    stack = []
    for x in nums:
        # 若要求最长单调非递减子序列, 则改成: idx = bisect_left(stack, x+1)
        idx = bisect_left(stack, x)
        if idx < len(stack):
            stack[idx] = x  # 下降
        else:
            stack.append(x)
    return len(stack)


def LIS2(nums: List[int]) -> int:
    """O(n^2)"""
    n = len(nums)
    dp = [1]*n
    for i, x in enumerate(nums):
        for j in range(i):
            y = nums[j]
            if x > y and (dp[j]+1) > dp[i]:
                dp[i] = dp[j]+1
    return max(dp)


def LCS(s1: str, s2: str) -> int:
    """请保证: len(s1) <= len(s2)"""
    m = len(s2)
    mapper = DefaultDict[str, List[int]](list)
    for i in reversed(range(m)):
        mapper[s2[i]].append(i)
    nums = []
    for c in s1:
        if c in mapper:
            nums.extend(mapper[c])
    return LIS(nums)


def LCS2(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        im = i-1  # minus
        for j in range(1, m+1):
            jm = j-1
            if s1[im] == s2[jm]:
                dp[i][j] = dp[im][jm]+1
            else:
                dp[i][j] = max(dp[im][j], dp[i][jm])
    return dp[n][m]


def _decode_LCS(s1: str, helper: List[List[int]]) -> str:
    res = bytearray()
    n, m = len(helper), len(helper[0])
    i, j = n-1, m-1
    while i > 0 and j > 0:
        if helper[i][j] == 0:
            res.append(ord(s1[i-1]))
            i -= 1
            j -= 1
        elif helper[i][j] == 1:
            i -= 1
        else:
            j -= 1
    res.reverse()
    return res.decode()


def LCS3(s1: str, s2: str) -> Tuple[int, str]:
    """新增功能: 输出LCS. 
    ref: 算法导论"""
    n, m = len(s1), len(s2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    helper = [[0] * (m+1) for _ in range(n+1)]  # 0,1,2
    for i in range(1, n+1):
        im = i-1
        for j in range(1, m+1):
            jm = j-1
            if s1[im] == s2[jm]:
                dp[i][j] = dp[im][jm]+1
            elif dp[im][j] > dp[i][jm]:
                dp[i][j] = dp[im][j]
                helper[i][j] = 1
            else:
                dp[i][j] = dp[i][jm]
                helper[i][j] = 2
    return dp[n][m], _decode_LCS(s1, helper)


def edit_distance(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j
    #
    for i in range(1, n+1):
        im = i-1
        for j in range(1, m+1):
            jm = j-1
            if s1[im] == s2[jm]:
                dp[i][j] = dp[im][jm]
            else:
                dp[i][j] = min(dp[im][j], dp[im][jm], dp[i][jm])+1
    return dp[n][m]


def matrix_chain(nums: List[int]) -> int:
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for hml in range(2, n):  # hi minus lo
        for lo in range(n-hml):
            hi = lo+hml
            dp[lo][hi] = INF
            for mid in range(lo+1, hi):
                r = dp[lo][mid]+dp[mid][hi]+nums[lo]*nums[mid]*nums[hi]
                if r < dp[lo][hi]:
                    dp[lo][hi] = r
    return dp[0][n-1]


def _decode_matrix_chain(helper: List[List[int]], lo: int, hi: int, res: bytearray) -> None:
    if hi-lo == 1:
        res += f"A{lo}".encode()
        return
    #
    res.append(ord("("))
    mid = helper[lo][hi]
    _decode_matrix_chain(helper, lo, mid, res)
    _decode_matrix_chain(helper, mid, hi, res)
    res.append(ord(")"))


def matrix_chain2(nums: List[int]) -> Tuple[int, str]:
    """新增功能: 输出chain结合的方式. 
    ref: 算法导论"""
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    helper = [[0] * n for _ in range(n)]  # mid: [1..n-2], 和0不冲突.
    for hml in range(2, n):  # hi minus lo
        for lo in range(n-hml):
            hi = lo+hml
            dp[lo][hi] = INF
            for mid in range(lo+1, hi):
                r = dp[lo][mid]+dp[mid][hi]+nums[lo]*nums[mid]*nums[hi]  # res
                if r < dp[lo][hi]:
                    dp[lo][hi] = r
                    helper[lo][hi] = mid
    res = bytearray()
    _decode_matrix_chain(helper, 0, n-1, res)
    return dp[0][n-1], res.decode()
