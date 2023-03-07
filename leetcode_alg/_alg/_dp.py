# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *


def LIS(nums: List[int]) -> int:
    """O(nlogn)"""
    stack = []
    for x in nums:
        idx = bisect_left(stack, x)
        if idx < len(stack):
            stack[idx] = x
        else:
            stack.append(x)
    return len(stack)


def LIS2(nums: List[int]) -> int:
    """O(n^2)"""
    n = len(nums)
    dp = [1]*n
    for i, x in enumerate(nums):
        for j, y in enumerate(nums[:i]):
            if x > y:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


def LCS(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        im = i-1
        for j in range(1, m+1):
            jm = j-1
            if s1[im] == s2[jm]:
                dp[i][j] = dp[im][jm]+1
            else:
                dp[i][j] = max(dp[im][j], dp[i][jm])
    return dp[n][m]


def _decode_LCS2(s1: str, helper: List[List[int]]) -> str:
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


def LCS2(s1: str, s2: str) -> Tuple[int, str]:
    """新增功能: 输出LCS. 
    ref: 算法导论"""
    # -:
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
    return dp[n][m], _decode_LCS2(s1, helper)


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
