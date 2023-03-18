# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *
from .._ds._heap import Heap, Heap2
from .._ds._union_find import UnionFind


def dijkstra(graph: List[Dict[int, int]], s: int) -> List[int]:
    """graph结合了邻接矩阵和邻接表的优点. graph[from_][to]->两节点的距离. O(1)
    无向图存两条边"""
    n = len(graph)
    dist = [INF] * n
    dist[s] = 0
    visited = bytearray(n)
    # 每次探索距离`s点`最近的节点
    pq = Heap[Tuple[int, int]]([])
    pq.push((0, s))
    while pq.heap:
        d, gn = pq.pop()  # graph node
        if visited[gn]:
            continue
        visited[gn] = False
        for to, d2 in graph[gn].items():
            new_d = d + d2  # 距离
            if new_d < dist[to]:
                dist[to] = new_d
                pq.push((new_d, to))
    return dist


def dijkstra2(graph: List[Dict[int, int]], s: int) -> List[int]:
    """use heap2. 令heap2中不存在冗余的gn(heap2是py实现, 不是C实现). 
    优点: C++实现时, 密集图时速度更快, 节约内存."""
    n = len(graph)
    dist = [INF] * n
    dist[s] = 0
    pq = Heap2[int]()
    pq.push((0, s))
    # visited数组可以省略
    while pq.heap:
        d, gn = pq.pop()
        for to, d2 in graph[gn].items():
            new_d = d + d2
            if new_d < dist[to]:
                dist[to] = new_d
                pq.push((new_d, to))
    return dist


def dijkstra3(graph: List[Dict[int, int]], s: int) -> List[int]:
    """类似于bfs实现, 优点: 在稀疏图时(|E|≈|V|)跑的很快"""
    n = len(graph)
    dist = [INF] * n
    dist[s] = 0
    dq = Deque[Tuple[int, int]]([(0, s)])
    #
    while dq:
        d, gn = dq.popleft()
        if d > dist[gn]:  # 使用dist数组充当visited的功能
            continue
        for to, d2 in graph[gn].items():
            new_d = d + d2
            if new_d < dist[to]:
                dist[to] = new_d
                dq.append((new_d, to))
    return dist


def kruskal(n: int, edges: List[Tuple[int, int, int]]) -> int:
    """edge: (gn, gn2, dist). 无向图存一条边"""
    edges.sort(key=itemgetter(2))
    uf = UnionFind(n)
    res = 0
    for gn, gn2, dist in edges:
        if n == 1:
            break
        if uf.union(gn, gn2):
            n -= 1
            res += dist
    return res


def prim(graph: List[Dict[int, int]]) -> int:
    """适合于稠密图. 无向图存两条边"""
    n = len(graph)
    res = 0
    cost = [INF] * n
    # 每次探索距离`已探索点集合`最近的节点
    pq = Heap[Tuple[int, int]]([])
    pq.push((0, 0))
    # visited数组可以省略, 使用cost.
    while pq.heap:
        d, gn = pq.pop()  # graph node
        if cost[gn] == 0:
            continue
        cost[gn] = 0
        res += d
        for to, d2 in graph[gn].items():
            if d2 < cost[to]:
                cost[to] = d2
                pq.push((d2, to))
    return res


def prim2(graph: List[Dict[int, int]]) -> int:
    """use heap2. 令heap2中不存在冗余的gn(heap2是py实现, 不是C实现). 
    优点: C++实现时, 密集图时速度更快, 节约内存."""
    n = len(graph)
    res = 0
    cost = [INF] * n
    pq = Heap2[int]()
    pq.push((0, 0))
    while pq.heap:
        d, gn = pq.pop()
        cost[gn] = 0
        res += d
        for to, d2 in graph[gn].items():
            if d2 < cost[to]:
                cost[to] = d2
                pq.push((d2, to))
    return res


def topo_sort(graph: List[List[int]]) -> List[int]:
    """graph: 邻接表实现. 有向图"""
    n = len(graph)
    res = []
    in_degree = [0] * n  # 入度
    for gn_list in graph:  # graph node
        for gn in gn_list:
            in_degree[gn] += 1
    #
    for i, in_d in enumerate(in_degree):
        if in_d == 0:
            res.append(i)
    #
    i = 0
    while i < len(res):
        gn = res[i]
        i += 1
        for gn2 in graph[gn]:
            in_degree[gn2] -= 1
            if in_degree[gn2] == 0:
                res.append(gn2)
    if len(res) != n:
        res = []
    return res


class Dinic:
    """最大流/最小割. 也可以解决二部图匹配问题. """

    def __init__(self, n: int) -> None:
        # 存正反边. 取反边: i^1.
        self.edges: List[Tuple[int, int]] = []  # [to, val]
        self.rg = [[] for _ in range(n)]  # residual graph. 存edge的索引

    def add_edge(self, from_: int, to: int, val: int) -> None:
        """val: 边容量"""
        en = len(self.edges)
        self.rg[from_].append(en)
        self.rg[to].append(en+1)
        self.edges += [(to, val), (from_, 0)]

    def _bfs(self, s: int, t: int) -> List[int]:
        # start, target
        n = len(self.rg)
        level = [-1] * n
        visited = bytearray(n)
        visited[s] = True
        dq = Deque[int]([s])
        dist = 0  # 距离
        while dq:
            dq_len = len(dq)
            for _ in range(dq_len):
                gn = dq.popleft()
                level[gn] = dist
                if gn == t:
                    break
                for idx in self.rg[gn]:
                    e = self.edges[idx]
                    to, val = e
                    if val == 0 or visited[to]:  # val一定满足>=0
                        continue
                    visited[to] = True
                    dq.append(to)
            dist += 1
        return level

    def _dfs(self, s: int, t: int, flow: int, level: List[int], idxs: List[int]) -> int:
        """
        idxs: 当前弧优化, 避免回溯. e.g. a->b,c->d
        """
        if s == t:
            return flow
        flow0 = flow
        es = self.rg[s]
        es_len = len(es)
        for i in range(idxs[s], es_len):
            e_idx = es[i]
            idxs[s] += 1
            to, val = self.edges[e_idx]
            if level[to] == level[s] or val == 0:  # 一定满足 level[to]>=level[s]
                continue
            f = self._dfs(to, t, min(val, flow), level, idxs)
            if f == 0:
                continue
            #
            from_, val2 = self.edges[e_idx ^ 1]
            self.edges[e_idx] = (to, val-f)
            self.edges[e_idx ^ 1] = (from_, val2+f)
            flow -= f
            if flow == 0:
                break
        return flow0 - flow

    def run(self, s: int, t: int) -> int:
        res = 0
        n = len(self.rg)
        while True:
            level = self._bfs(s, t)
            if level[t] == -1:
                break
            idxs = [0] * n
            res += self._dfs(s, t, INF, level, idxs)
        return res


def _match(graph: List[List[int]], gn: int, visited: bytearray, matching: List[int]) -> bool:
    """匹配gn节点"""
    if visited[gn]:
        return False
    visited[gn] = True
    for gn2 in graph[gn]:
        gn3 = matching[gn2]
        if gn3 == -1 or _match(graph, gn3, visited, matching):
            matching[gn2] = gn
            return True
    return False


def hungarian(graph: List[List[int]]) -> int:
    """graph: 邻接表实现. 无向图存单边即可(部1->部2)
    匹配大小的最大值=顶点覆盖大小的最小值(覆盖所有边)
    独立集大小的最大值=边覆盖大小的最小值(覆盖所有顶点)
    匹配大小的最大值=n-独立集大小的最大值(n为顶点数)
    """
    n = len(graph)
    res = 0
    matching = [-1] * n  # 匹配情况. (只存部2->部1的边)
    for gn in range(n):
        visited = bytearray(n)  # (部1的visited)
        if _match(graph, gn, visited, matching):
            res += 1
    return res
