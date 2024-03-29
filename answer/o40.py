from leetcode_alg import *

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        quick_select(arr, k-1)
        return arr[:k]

class Solution2:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        res = []
        heap = Heap(arr)
        for _ in range(k):
            res.append(heap.pop())
        return res


class Solution3:
    """faster"""
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]


class Solution4:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        res = heapq.nsmallest(k, arr)
        return res

if __name__ == "__main__":
    arr = [0,1,2,1]
    k = 1
    assert Solution().getLeastNumbers(arr, k) == [0]
    assert Solution2().getLeastNumbers(arr[:], k) == [0]
    assert Solution3().getLeastNumbers(arr, k) == [0]
    assert Solution4().getLeastNumbers(arr, k) == [0]
