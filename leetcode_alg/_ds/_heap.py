# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *
import heapq


try:
    heapify_max = heapq._heapify_max  # C
except AttributeError:
    def heapify_max(heap: List[int]) -> None:
        n = len(heap)
        for i in reversed(range(n >> 1)):
            heapq._siftup_max(heap, i)  # 下滤

try:
    heapreplace_max = heapq._heapreplace_max
except AttributeError:
    def heapreplace_max(heap: List[int], x: int) -> int:
        assert len(heap) > 0
        x, heap[0] = heap[0], x
        heapq._siftup_max(heap, 0)
        return x
try:
    heappop_max = heapq._heappop_max
except AttributeError:
    def heappop_max(heap: List[int]) -> int:
        res = heap.pop()
        if len(heap) == 0:
            return res
        #
        res, heap[0] = heap[0], res
        heapq._siftup_max(heap, 0)
        return res


def heappush_max(heap: List[int], x: int) -> None:
    heap.append(x)
    heapq._siftdown_max(heap, 0, len(heap)-1)  # 上滤


def heappushpop_max(heap: List[int], x: int) -> int:
    if len(heap) == 0 or x >= heap[0]:
        return x
    #
    x, heap[0] = heap[0], x
    heapq._siftup_max(heap, 0)
    return x
#


class Heap:
    def __init__(self, nums: List[int], max_heap: bool = False, need_heapify: bool = True) -> None:
        """
        nums: not const
        need_heapify: 如果nums已有序, 可以令need_heapify=False
        """
        if max_heap:
            self._heapify = heapify_max
            self._heappush = heappush_max
            self._heappop = heappop_max
            self._heapreplace = heapreplace_max
            self._heappushpop = heappushpop_max
        else:
            self._heapify = heapify
            self._heappush = heappush
            self._heappop = heappop
            self._heapreplace = heapreplace
            self._heappushpop = heappushpop
        #
        self.heap = nums
        if len(nums) > 1 and need_heapify:
            self._heapify(self.heap)

    def push(self, x: int) -> None:
        self._heappush(self.heap, x)

    def pop(self) -> int:
        return self._heappop(self.heap)

    def replace(self, x: int) -> int:
        return self._heapreplace(self.heap, x)

    def pushpop(self, x: int) -> int:
        return self._heappushpop(self.heap, x)

    def top(self) -> int:
        return self.heap[0]

    def __len__(self) -> int:
        return len(self.heap)


class Heap2:
    """增加的功能: 可以通过id, 动态的调整val; 可以通过id, 动态的删除"""

    def __init__(self, key: Optional[Callable[[int, int], int]] = None) -> None:
        self.heap: List[Tuple[int, int]] = []  # val, id
        self._id2pos: Dict[int, int] = {}  # id->pos

        if key is None:
            key = lt
            # max_heap: gt
        self._key_func = key

    def _siftup(self, i: int) -> None:
        """上滤. (命名与python的heapq库相反)"""
        heap, id2pos = self.heap, self._id2pos
        x0 = heap[i]
        while i > 0:  # 即pi >= 0
            pi = (i-1) >> 1
            px = heap[pi]
            if not self._key_func(x0, px):
                break
            heap[i], id2pos[px[1]] = px, i
            i = pi
        heap[i], id2pos[x0[1]] = x0, i

    def _siftdown(self, i: int) -> None:
        """下滤"""
        heap, id2pos = self.heap, self._id2pos
        n = len(heap)
        x0 = heap[i]
        while True:
            ci = (i << 1)+1
            if ci >= n:
                break
            if ci+1 < n and self._key_func(heap[ci+1], heap[ci]):
                ci += 1
            cx = heap[ci]
            if not self._key_func(cx, x0):
                break
            heap[i], id2pos[cx[1]] = cx, i
            i = ci
        heap[i], id2pos[x0[1]] = x0, i

    def _heapify(self) -> None:
        n = len(self.heap)
        for i in reversed(range(n >> 1)):
            self._siftdown(i)

    def push(self, x: Tuple[int, int]) -> None:
        """x: val, id"""
        heap, id2pos = self.heap, self._id2pos
        if x[1] in id2pos:  # 修改
            heap, id2pos = self.heap, self._id2pos
            pos = id2pos[x[1]]
            z = heap[pos]
            heap[pos] = x
            if self._key_func(z, x):
                self._siftdown(pos)
            else:
                self._siftup(pos)
        else:  # 添加
            n = len(heap)
            heap.append(x)
            id2pos[x[1]] = n
            self._siftup(n)

    def remove(self, id: int) -> int:
        """O(logn)"""
        heap, id2pos = self.heap, self._id2pos
        pos = id2pos.pop(id)
        n = len(self.heap)
        heap[pos], heap[n-1] = heap[n-1], heap[pos]
        id2pos[heap[pos][1]] = pos
        res = heap.pop()
        self._siftdown(pos)
        return res[1]

    def pop(self) -> Tuple[int, int]:
        """return: val, id"""
        heap, id2pos = self.heap, self._id2pos
        res = heap.pop()
        if len(heap) == 0:
            return res
        #
        res, heap[0] = heap[0], res
        id2pos.pop(res[1])
        self._siftdown(0)
        return res

    def replace(self, x: Tuple[int, int]) -> Tuple[int, int]:
        heap, id2pos = self.heap, self._id2pos
        assert len(heap) > 0
        res = heap[0]
        id2pos.pop(res[1])
        heap[0], id2pos[x[1]] = x, 0
        self._siftdown(0)
        return res

    def pushpop(self, x: Tuple[int, int]) -> Tuple[int, int]:
        heap, id2pos = self.heap, self._id2pos
        if len(heap) == 0 or self._key_func(x, heap[0]):
            return x
        #
        res = heap[0]
        id2pos.pop(res[1])
        heap[0], id2pos[x[1]] = x, 0
        self._siftdown(0)
        return x

    def top(self) -> Tuple[int, int]:
        """O(1). return: val, id"""
        return self.heap[0]

    def __len__(self) -> int:
        return len(self.heap)

    def __getitem__(self, id: int) -> int:
        """O(1)"""
        pos = self._id2pos[id]
        return self.heap[pos][0]

    def __setitem__(self, id: int, val: int) -> None:
        """O(logn)"""
        self.push((val, id))

    def __delitem__(self, id: int) -> None:
        self.remove(id)

    def __contains__(self, id: int) -> bool:
        """O(1)"""
        return id in self._id2pos
