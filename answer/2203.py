
from leetcode_alg import *


class Solution:
    """recommended"""
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph: List[Dict[int, int]] = [{} for _ in range(n)]
        graph_r: List[Dict[int, int]] = [{} for _ in range(n)]
        for e in edges:
            gn, to, val = e
            if to in graph[gn]:
                graph[gn][to] = min(graph[gn][to], val)  # 重边
                graph_r[to][gn] = min(graph_r[to][gn], val)
            else:
                graph[gn][to] = val
                graph_r[to][gn] = val
        res3 = dijkstra(graph_r, dest)
        if res3[src1] == INF or res3[src2] == INF:
            return -1
        res1 = dijkstra(graph, src1)
        res2 = dijkstra(graph, src2)
        res = INF
        for r123 in zip(res1, res2, res3):
            res = min(res, sum(r123))
        return res


class Solution2:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph: List[Dict[int, int]] = [{} for _ in range(n)]
        graph_r: List[Dict[int, int]] = [{} for _ in range(n)]
        for e in edges:
            gn, to, val = e
            if to in graph[gn]:
                graph[gn][to] = min(graph[gn][to], val)  # 重边
                graph_r[to][gn] = min(graph_r[to][gn], val)
            else:
                graph[gn][to] = val
                graph_r[to][gn] = val
        res3 = dijkstra2(graph_r, dest)
        if res3[src1] == INF or res3[src2] == INF:
            return -1
        res1 = dijkstra2(graph, src1)
        res2 = dijkstra2(graph, src2)
        res = INF
        for r123 in zip(res1, res2, res3):
            res = min(res, sum(r123))
        return res


if __name__ == "__main__":
    n = 6
    edges = [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3], [2, 3, 4], [3, 4, 2], [4, 5, 1]]
    src1 = 0
    src2 = 1
    dest = 5
    print(Solution().minimumWeight(n, edges, src1, src2, dest))
    print(Solution2().minimumWeight(n, edges, src1, src2, dest))
