from leetcode_alg import *


class Solution:
    """recommended. 最小生成树"""

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = [{} for _ in range(n)]
        for i, (x, y) in enumerate(points):
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x) + abs(y2 - y)
                graph[i][j] = dist
                graph[j][i] = dist
        return prim2(graph)


class Solution2:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i, (x, y) in enumerate(points):
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x) + abs(y2 - y)
                edges.append((i, j, dist))
        return kruskal(n, edges)


class Solution3:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = [{} for _ in range(n)]
        for i, (x, y) in enumerate(points):
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x) + abs(y2 - y)
                graph[i][j] = dist
                graph[j][i] = dist
        return prim(graph)


if __name__ == "__main__":
    x = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    assert Solution().minCostConnectPoints(x) == 20
    assert Solution2().minCostConnectPoints(x) == 20
    assert Solution3().minCostConnectPoints(x) == 20
