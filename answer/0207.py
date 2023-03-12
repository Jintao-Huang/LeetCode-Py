from leetcode_alg import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for to, from_ in prerequisites:
            graph[from_].append(to)
        return len(topo_sort(graph)) > 0

if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    assert Solution().canFinish(numCourses, prerequisites) is True