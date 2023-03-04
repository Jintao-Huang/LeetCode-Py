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
    pq = Heap([])
    pq.push((0, s))
    while len(pq) > 0:
        d, gn = pq.pop()  # graph node
        if visited[gn] == True:
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
    优点: C++实现时速度更快."""
    n = len(graph)
    dist = [INF] * n
    dist[s] = 0
    pq = Heap2()
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
    pq = Heap([])
    pq.push((0, 0))
    # visited数组可以省略, 与cost数组合一.
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
    优点: C++实现时速度更快."""
    n = len(graph)
    res = 0
    cost = [INF] * n
    pq = Heap2()
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
