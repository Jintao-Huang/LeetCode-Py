
from leetcode_alg import *


def dfs(grid: List[List[str]], i: int, j: int) -> None:
    grid[i][j] = "0"
    n, m = len(grid), len(grid[0])
    if i > 0 and grid[i-1][j] == "1":
        dfs(grid, i-1, j)
    if j > 0 and grid[i][j-1] == "1":
        dfs(grid, i, j-1)
    if i < n-1 and grid[i+1][j] == "1":
        dfs(grid, i+1, j)
    if j < m-1 and grid[i][j+1] == "1":
        dfs(grid, i, j+1)


class Solution:
    """recommended"""

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i, gr in enumerate(grid):
            for j, g in enumerate(gr):
                if g == "1":
                    res += 1
                    dfs(grid, i, j)
        return res


def bfs(grid: List[List[str]], i: int, j: int) -> None:
    dq = Deque[Tuple[int, int]]([(i, j)])
    n, m = len(grid), len(grid[0])
    while len(dq) > 0:
        i, j = dq.popleft()
        if i > 0 and grid[i-1][j] == "1":
            grid[i-1][j] = "0"
            dq.append((i-1, j))
        if j > 0 and grid[i][j-1] == "1":
            grid[i][j-1] = "0"
            dq.append((i, j-1))
        if i < n-1 and grid[i+1][j] == "1":
            grid[i+1][j] = "0"
            dq.append((i+1, j))
        if j < m-1 and grid[i][j+1] == "1":
            grid[i][j+1] = "0"
            dq.append((i, j+1))


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i, gr in enumerate(grid):
            for j, g in enumerate(gr):
                if g == "1":
                    res += 1
                    bfs(grid, i, j)
        return res


class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0
        uf = UnionFind(n*m)
        #
        for i, gr in enumerate(grid):
            for j, g in enumerate(gr):
                if g == "1":
                    res += 1
                    idx = i*m+j
                    if i > 0 and grid[i-1][j] == "1" and uf.union(idx, idx-m):
                        res -= 1
                    if j > 0 and grid[i][j-1] == "1" and uf.union(idx, idx-1):
                        res -= 1
        return res


if __name__ == "__main__":
    grid = [["1", "1", "1"], ["1", "0", "1"], ["1", "1", "1"]]
    assert Solution().numIslands(deepcopy(grid)) == 1
    assert Solution2().numIslands(deepcopy(grid)) == 1
    assert Solution3().numIslands(deepcopy(grid)) == 1

