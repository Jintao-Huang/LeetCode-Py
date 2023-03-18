
from leetcode_alg import *


class Solution:
    """recommended. 标准做法. 最短路径, 中心法."""

    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph: List[Dict[int, int]] = [{} for _ in range(n)]
        graph_r: List[Dict[int, int]] = [{} for _ in range(n)]
        for e in edges:
            gn, to, val = e
            if to not in graph[gn]:
                graph[gn][to] = val
                graph_r[to][gn] = val
            elif val < graph[gn][to]:
                graph[gn][to] = val  # 重边
                graph_r[to][gn] = val
        res3 = dijkstra(graph_r, dest)
        if res3[src1] == INF or res3[src2] == INF:
            return -1
        res1 = dijkstra(graph, src1)
        res2 = dijkstra(graph, src2)
        res = INF
        for r1, r2, r3 in zip(res1, res2, res3):
            r = r1+r2+r3
            if r < res:
                res = r
        return res


class Solution2:
    """faster. 稀疏图优化"""

    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph: List[Dict[int, int]] = [{} for _ in range(n)]
        graph_r: List[Dict[int, int]] = [{} for _ in range(n)]
        for e in edges:
            gn, to, val = e
            if to not in graph[gn]:
                graph[gn][to] = val
                graph_r[to][gn] = val
            elif val < graph[gn][to]:
                graph[gn][to] = val  # 重边
                graph_r[to][gn] = val
        res3 = dijkstra3(graph_r, dest)
        if res3[src1] == INF or res3[src2] == INF:
            return -1
        res1 = dijkstra3(graph, src1)
        res2 = dijkstra3(graph, src2)
        res = INF
        for r1, r2, r3 in zip(res1, res2, res3):
            r = r1+r2+r3
            if r < res:
                res = r
        return res


class Solution3:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph: List[Dict[int, int]] = [{} for _ in range(n)]
        graph_r: List[Dict[int, int]] = [{} for _ in range(n)]
        for e in edges:
            gn, to, val = e
            if to not in graph[gn]:
                graph[gn][to] = val
                graph_r[to][gn] = val
            elif val < graph[gn][to]:
                graph[gn][to] = val  # 重边
                graph_r[to][gn] = val
        res3 = dijkstra2(graph_r, dest)
        if res3[src1] == INF or res3[src2] == INF:
            return -1
        res1 = dijkstra2(graph, src1)
        res2 = dijkstra2(graph, src2)
        res = INF
        for r1, r2, r3 in zip(res1, res2, res3):
            r = r1+r2+r3
            if r < res:
                res = r
        return res


if __name__ == "__main__":
    n = 6
    edges = [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3], [2, 3, 4], [3, 4, 2], [4, 5, 1]]
    src1 = 0
    src2 = 1
    dest = 5
    assert Solution().minimumWeight(n, edges, src1, src2, dest) == 9
    assert Solution2().minimumWeight(n, edges, src1, src2, dest) == 9
    assert Solution3().minimumWeight(n, edges, src1, src2, dest) == 9
