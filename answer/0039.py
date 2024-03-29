from leetcode_alg import *


def dfs(candidates: List[int], idx: int, target: int,
        path: List[int], res: List[List[int]]) -> None:
    if target == 0:
        res.append(path[:])  # 浅copy
        return
    n = len(candidates)
    for i in range(idx, n):
        c = candidates[i]
        if target < c:
            break
        path.append(c)
        dfs(candidates, i, target - c, path, res)
        path.pop()


class Solution:
    """recommended. 回溯"""

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        dfs(candidates, 0, target, [], res)
        return res


class Solution2:
    """also recommended. 从完全背包改编. """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp: List[List[List[int]]] = [[] for _ in range(target+1)]
        #
        for c in candidates:
            for capa in range(c, target+1):
                c2 = capa-c
                if c2 == 0:
                    dp[capa].append([c])
                if dp[c2]:
                    for r in dp[c2]:
                        rc = r[:]  # res copy
                        rc.append(c)
                        dp[capa].append(rc)
        return dp[target]


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    assert Solution().combinationSum(candidates, target) == [[2, 2, 3], [7]]
    assert Solution2().combinationSum(candidates, target) == [[2, 2, 3], [7]]
