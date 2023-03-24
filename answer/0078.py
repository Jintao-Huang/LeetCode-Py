
from leetcode_alg import *


def dfs(nums: List[int], idx: int, path: List[int], res: List[List[int]]) -> None:
    res.append(path[:])
    n = len(nums)
    for i in range(idx, n):
        path.append(nums[i])
        dfs(nums, i+1, path, res)
        path.pop()

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        dfs(nums, 0, [], res)
        return res

class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return subsets(nums)

class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(n + 1):
            ans += combinations(nums, i)
        return ans
    
if __name__ == "__main__":
    nums = [1,2,3]
    assert Solution().subsets(nums) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    assert Solution2().subsets(nums) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert Solution3().subsets(nums) == [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
