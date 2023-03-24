from leetcode_alg import *


def dfs(nums: List[int], idx: int, path: List[int], res: List[List[int]]) -> None:
    res.append(path[:])
    n = len(nums)
    for i in range(idx, n):
        if i > idx and nums[i] == nums[i-1]:
            continue
        path.append(nums[i])
        dfs(nums, i+1, path, res)
        path.pop()


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        dfs(nums, 0, [], res)
        return res


if __name__ == "__main__":
    nums = [1, 2, 2]
    assert Solution().subsetsWithDup(nums) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
