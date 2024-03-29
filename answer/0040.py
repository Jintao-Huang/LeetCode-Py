from leetcode_alg import *


def dfs(candidates: List[int], idx: int, target: int,
        path: List[int], res: List[List[int]]) -> None:
    if target == 0:
        res.append(path[:])
        return
    n = len(candidates)
    for i in range(idx, n):
        c = candidates[i]
        if target < c:
            break
        if i > idx and c == candidates[i-1]:  # 去重
            continue
        path.append(c)
        dfs(candidates, i+1, target - c, path, res)
        path.pop()


class Solution:
    """回溯"""
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        dfs(candidates, 0, target, [], res)
        return res


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    assert Solution().combinationSum2(candidates, target) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
