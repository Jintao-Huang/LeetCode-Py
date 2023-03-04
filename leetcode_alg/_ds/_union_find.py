# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [1] * n  # 代表每个集合的数量. 只有root的值有效. 使用方法: self.rank[find_root(i)]

    def find_root(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find_root(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        ri, rj = self.find_root(i), self.find_root(j)
        if ri == rj:
            return False
        if self.rank[ri] < self.rank[rj]:
            ri, rj = rj, ri
        self.parent[rj] = ri
        # ref: https://oi-wiki.org/ds/dsu/#%E5%90%AF%E5%8F%91%E5%BC%8F%E5%90%88%E5%B9%B6
        # 选择节点较少的树连到另一棵, 也可以选择深度较小的树
        self.rank[ri] += self.rank[rj]
        return True
