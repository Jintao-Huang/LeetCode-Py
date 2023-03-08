# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *
from .._ds._heap import Heap, Heap2
from .._ds._union_find import UnionFind


def dijkstra(graph: List[Dict[int, int]], s: int) -> List[int]:
    """graph结合了邻接矩阵和邻接表的优点. graph[from_][to]->distant. O(1)
    无向图存两条边"""
    n = len(graph)
    dist = [INF] * n
    dist[s] = 0
    visited = bytearray(n)
    # 每次探索距离`s点`最近的节点
    pq = Heap[Tuple[int, int]]([])
    pq.push((0, s))
    while len(pq) > 0:
        d, gn = pq.pop()  # graph node
        if visited[gn]:
            continue
        visited[gn] = False
        for to, d2 in graph[gn].items():
            new_d = d + d2  # 距离
            if dist[to] <= new_d:
                continue
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
    while len(pq) > 0:
        d, gn = pq.pop()
        for to, d2 in graph[gn].items():
            new_d = d + d2
            if dist[to] <= new_d:
                continue
            dist[to] = new_d
            pq.push((new_d, to))
    return dist


def dijkstra3(graph: List[Dict[int, int]], s: int) -> List[int]:
    """类似于bfs实现, 优点: 在稀疏图时(|E|≈|V|)跑的很快
    不同于标准bfs. 这里不能设计visited数组. 使用dist数组充当weak visited的功能
    """
    n = len(graph)
    dist = [INF] * n
    dist[s] = 0
    dq = Deque[int]([s])
    # 
    while len(dq) > 0:
        gn = dq.popleft()
        d = dist[gn]
        for to, d2 in graph[gn].items():
            new_d = d + d2
            if dist[to] <= new_d:
                continue
            dist[to] = new_d
            dq.append(to)
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
    while len(pq) > 0:
        d, gn = pq.pop()  # graph node
        if cost[gn] == 0:
            continue
        cost[gn] = 0
        res += d
        for to, d2 in graph[gn].items():
            if cost[to] <= d2:
                continue
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
    while len(pq) > 0:
        d, gn = pq.pop()
        cost[gn] = 0
        res += d
        for to, d2 in graph[gn].items():
            if cost[to] <= d2:
                continue
            cost[to] = d2
            pq.push((d2, to))
    return res


def topo_sort(graph: List[List[int]]) -> List[int]:
    """graph: 邻接表实现"""
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
