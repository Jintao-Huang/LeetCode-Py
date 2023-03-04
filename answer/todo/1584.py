from leetcode_alg import *


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = [{} for _ in range(n)]
        for i, (x, y) in enumerate(points):
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = manhattan_dist(x, y, x2, y2)
                graph[i][j] = dist
                graph[j][i] = dist
        return prim(graph)


class Solution2:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i, (x, y) in enumerate(points):
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = manhattan_dist(x, y, x2, y2)
                edges.append((i, j, dist))
        return kruskal(n, edges)

class Solution3:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = [{} for _ in range(n)]
        for i, (x, y) in enumerate(points):
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = manhattan_dist(x, y, x2, y2)
                graph[i][j] = dist
                graph[j][i] = dist
        return prim2(graph)

if __name__ == "__main__":
    x = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(Solution().minCostConnectPoints(x))
    print(Solution2().minCostConnectPoints(x))
    print(Solution3().minCostConnectPoints(x))
