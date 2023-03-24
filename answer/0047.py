from leetcode_alg import *


def dfs(nums: List[int], visited: List[bool],
        path: List[int], res: List[List[int]]) -> None:
    n = len(nums)
    if len(path) == n:
        res.append(path[:])
        return

    for i, x in enumerate(nums):
        if visited[i] or (i > 0 and not visited[i-1] and x == nums[i-1]):
            continue
        #
        path.append(x)
        visited[i] = True
        dfs(nums, visited, path, res)
        path.pop()
        visited[i] = False


class Solution:
    """回溯"""
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [False] * len(nums)
        res = []
        dfs(nums, visited, [], res)
        return res


class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums)))   # leetcode不检查list和tuple.


if __name__ == "__main__":
    nums = [1, 1]
    assert Solution().permuteUnique(nums) == [[1, 1]]
    assert Solution2().permuteUnique(nums) == [(1, 1)]
