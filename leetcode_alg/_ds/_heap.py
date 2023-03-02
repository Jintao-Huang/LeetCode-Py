
import heapq
from typing import List, Tuple, Dict, Callable, Optional
from heapq import (
    heapify, heappop, heappush, heappushpop, heapreplace,
)

try:
    heapify_max = heapq._heapify_max  # C
except AttributeError:
    def heapify_max(heap: List[int]) -> None:
        n = len(heap)
        for i in reversed(range(n//2)):
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
        if need_heapify:
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

    def __init__(self, nums: List[Tuple[int, int]], max_heap: bool = False, need_heapify: bool = True) -> None:
        """nums: id, val"""
        self.heap: List[Tuple[int, int]] = nums  # id, val
        self._id2pos: Dict[int, int] = {x[0]: i for i, x in enumerate(nums)}  # id->pos

        if max_heap:
            self._keys_func = lambda x, y: x[1] > y[1]
        else:
            self._keys_func = lambda x, y: x[1] < y[1]
        if need_heapify:
            self._heapify()

    def _siftup(self, i: int) -> None:
        """上滤"""
        heap, id2pos = self.heap, self._id2pos
        x0 = heap[i]
        while True:
            pi = (i-1) >> 1
            if pi < 0:
                break
            px = heap[pi]
            if not self._keys_func(x0, px):
                break
            heap[i], id2pos[px[0]] = px, i
            i = pi
        heap[i], id2pos[x0[0]] = x0, i

    def _siftdown(self, i: int) -> None:
        """下滤"""
        heap, id2pos = self.heap, self._id2pos
        n = len(heap)
        x0 = heap[i]
        while True:
            ci = (i << 1)+1
            if ci >= n:
                break
            if ci+1 < n and self._keys_func(heap[ci+1], heap[ci]):
                ci += 1
            cx = heap[ci]
            if not self._keys_func(cx, x0):
                break
            heap[i], id2pos[cx[0]] = cx, i
            i = ci
        heap[i], id2pos[x0[0]] = x0, i

    def _heapify(self) -> None:
        n = len(self.heap)
        for i in reversed(range(n//2)):
            self._siftdown(i)

    def push(self, x: Tuple[int, int]) -> None:
        heap, id2pos = self.heap, self._id2pos
        if x[0] in id2pos:  # 修改
            heap, id2pos = self.heap, self._id2pos
            pos = id2pos[x[0]]
            z = heap[pos]
            heap[pos] = x
            if self._keys_func(z, x):
                self._siftdown(pos)
            else:
                self._siftup(pos)
        else:  # 添加
            n = len(heap)
            heap.append(x)
            id2pos[x[0]] = n
            self._siftup(n)

    def pop(self) -> Tuple[int, int]:
        heap, id2pos = self.heap, self._id2pos
        res = heap.pop()
        if len(heap) == 0:
            return res
        #
        res, heap[0] = heap[0], res
        id2pos.pop(res[0])
        self._siftdown(0)
        return res

    def replace(self, x: Tuple[int, int]) -> Tuple[int, int]:
        heap, id2pos = self.heap, self._id2pos
        assert len(heap) > 0
        res = heap[0]
        id2pos.pop(res[0])
        heap[0], id2pos[x[0]] = x, 0
        self._siftdown(0)
        return res

    def pushpop(self, x: Tuple[int, int]) -> Tuple[int, int]:
        heap, id2pos = self.heap, self._id2pos
        if len(heap) == 0 or self._keys_func(x, heap[0]):
            return x
        #
        res = heap[0]
        id2pos.pop(res[0])
        heap[0], id2pos[x[0]] = x, 0
        self._siftdown(0)
        return x

    def __len__(self) -> int:
        return len(self.heap)

    def __getitem__(self, id: int) -> int:
        """O(1)"""
        pos = self._id2pos[id]
        return self.heap[pos][1]

    def __setitem__(self, id: int, val: int) -> None:
        """O(logn)"""
        self.push((id, val))

    def __delitem__(self, id: int) -> None:
        """O(logn)"""
        heap, id2pos = self.heap, self._id2pos
        pos = id2pos.pop(id)
        n = len(self.heap)
        heap[pos], heap[n-1] = heap[n-1], heap[pos]
        id2pos[heap[pos][0]] = pos
        heap.pop()
        self._siftdown(pos)

    def __contains__(self, id: int) -> bool:
        """O(1)"""
        return id in self._id2pos
