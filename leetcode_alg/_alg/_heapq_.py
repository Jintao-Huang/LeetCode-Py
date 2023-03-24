# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *
from .._ds._heap import heapify_max, heapreplace_max, heappop_max


def _nlargest_smallest(nums: List[int], n: int, mode: Literal["nlargest", "nsmallest"]) -> List[int]:
    if mode == "nlargest":
        _heapify = heapify
        _heapreplace = heapreplace
        comp = gt
    else:
        _heapify = heapify_max
        _heapreplace = heapreplace_max
        comp = lt
    #
    heap = nums[:n]
    _heapify(heap)
    for x in nums[n:]:
        if comp(x, heap[0]):
            _heapreplace(heap, x)
    return heap


def nlargest_(nums: List[int], n: int) -> List[int]:
    """不稳定(heap.nlargest是稳定的). 使用小根堆"""
    return _nlargest_smallest(nums, n, "nlargest")


def nsmallest_(nums: List[int], n: int) -> List[int]:
    """不稳定(heap.nsmallest是稳定的). 使用大根堆"""
    return _nlargest_smallest(nums, n, "nsmallest")


def merge_heapq_(*nums_list: List[int], max_heap: bool = False) -> List[int]:
    if max_heap:
        _heapify = heapify_max
        _heappop = heappop_max
        _heapreplace = heapreplace_max
    else:
        _heapify = heapify
        _heappop = heappop
        _heapreplace = heapreplace
    #
    heap = []
    res = []
    for nums in nums_list:
        it = iter(nums)
        try:
            heap.append((next(it), it))
        except StopIteration:
            pass
    #
    _heapify(heap)
    while len(heap) > 1:
        x, it = heap[0]
        res.append(x)
        try:
            _heapreplace(heap, (next(it), it))
        except StopIteration:
            _heappop(heap)
    x, it = heap[0]
    res.append(x)
    res += list(it)
    return res
