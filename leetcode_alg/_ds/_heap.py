# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *
import heapq
_T = TypeVar("_T")

try:
    heapify_max = heapq._heapify_max  # C
except AttributeError:
    def heapify_max(heap: List[Any]) -> None:
        n = len(heap)
        for i in reversed(range(n >> 1)):
            heapq._siftup_max(heap, i)  # 下滤

try:
    heapreplace_max = heapq._heapreplace_max
except AttributeError:
    def heapreplace_max(heap: List[_T], x: _T) -> _T:
        assert len(heap) > 0
        x, heap[0] = heap[0], x
        heapq._siftup_max(heap, 0)
        return x
try:
    heappop_max = heapq._heappop_max
except AttributeError:
    def heappop_max(heap: List[_T]) -> _T:
        res = heap.pop()
        if len(heap) == 0:
            return res
        #
        res, heap[0] = heap[0], res
        heapq._siftup_max(heap, 0)
        return res


def heappush_max(heap: List[_T], x: _T) -> None:
    heap.append(x)
    heapq._siftdown_max(heap, 0, len(heap)-1)  # 上滤


def heappushpop_max(heap: List[_T], x: _T) -> _T:
    if len(heap) == 0 or x >= heap[0]:
        return x
    #
    x, heap[0] = heap[0], x
    heapq._siftup_max(heap, 0)
    return x
#


class Heap(Generic[_T]):
    def __init__(self, nums: List[_T], max_heap: bool = False, need_heapify: bool = True) -> None:
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

    def push(self, x: _T) -> None:
        self._heappush(self.heap, x)

    def pop(self) -> _T:
        return self._heappop(self.heap)

    def replace(self, x: _T) -> _T:
        return self._heapreplace(self.heap, x)

    def pushpop(self, x: _T) -> _T:
        return self._heappushpop(self.heap, x)


class Heap2(Generic[_T]):
    """增加的功能: 可以通过id, 动态的调整val; 可以通过id, 动态的删除"""

    def __init__(self, comp: Callable[[_T, _T], bool] = lt) -> None:
        # max_heap: gt
        self.heap: List[Tuple[_T, int]] = []  # val, id
        self._id2pos: Dict[int, int] = {}  # id->pos
        self._comp = comp

    def _siftup(self, i: int) -> None:
        """上滤. (命名与python的heapq库相反)"""
        heap, id2pos = self.heap, self._id2pos
        x0 = heap[i]
        while i > 0:  # 即pi >= 0
            pi = (i-1) >> 1
            px = heap[pi]
            if not self._comp(x0[0], px[0]):
                break
            heap[i], id2pos[px[1]] = px, i
            i = pi
        heap[i], id2pos[x0[1]] = x0, i

    def _siftdown(self, i: int) -> None:
        """下滤"""
        heap, id2pos = self.heap, self._id2pos
        n = len(heap)
        x0 = heap[i]
        while (ci := (i << 1)+1) < n:  # python>=3.8
            if ci+1 < n and self._comp(heap[ci+1][0], heap[ci][0]):
                ci += 1
            cx = heap[ci]
            if not self._comp(cx[0], x0[0]):
                break
            heap[i], id2pos[cx[1]] = cx, i
            i = ci
        heap[i], id2pos[x0[1]] = x0, i

    def _heapify(self) -> None:
        n = len(self.heap)
        for i in reversed(range(n >> 1)):
            self._siftdown(i)

    def push(self, x: Tuple[_T, int]) -> None:
        """x: val, id"""
        heap, id2pos = self.heap, self._id2pos
        if x[1] in id2pos:  # 修改
            heap, id2pos = self.heap, self._id2pos
            pos = id2pos[x[1]]
            z = heap[pos]
            heap[pos] = x
            if self._comp(z[0], x[0]):
                self._siftdown(pos)
            else:
                self._siftup(pos)
        else:  # 添加
            n = len(heap)
            heap.append(x)
            id2pos[x[1]] = n
            self._siftup(n)

    def remove(self, id: int) -> _T:
        """O(logn)"""
        heap, id2pos = self.heap, self._id2pos
        pos = id2pos.pop(id)
        n = len(self.heap)
        heap[pos], heap[n-1] = heap[n-1], heap[pos]
        id2pos[heap[pos][1]] = pos
        res = heap.pop()
        self._siftdown(pos)
        return res[0]

    def pop(self) -> Tuple[_T, int]:
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

    def replace(self, x: Tuple[_T, int]) -> Tuple[_T, int]:
        heap, id2pos = self.heap, self._id2pos
        assert len(heap) > 0
        res = heap[0]
        id2pos.pop(res[1])
        heap[0], id2pos[x[1]] = x, 0
        self._siftdown(0)
        return res

    def pushpop(self, x: Tuple[_T, int]) -> Tuple[_T, int]:
        heap, id2pos = self.heap, self._id2pos
        if len(heap) == 0 or self._comp(x[0], heap[0][0]):
            return x
        #
        res = heap[0]
        id2pos.pop(res[1])
        heap[0], id2pos[x[1]] = x, 0
        self._siftdown(0)
        return x

    def __getitem__(self, id: int) -> _T:
        """O(1)"""
        pos = self._id2pos[id]
        return self.heap[pos][0]

    def __setitem__(self, id: int, val: _T) -> None:
        """O(logn)"""
        self.push((val, id))

    def __delitem__(self, id: int) -> None:
        self.remove(id)

    def __contains__(self, id: int) -> bool:
        """O(1)"""
        return id in self._id2pos
