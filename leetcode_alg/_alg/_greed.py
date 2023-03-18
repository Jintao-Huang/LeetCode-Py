from .._types import *


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """请保证输入的intervals按start有序 
    为什么按start排序比按end排序更优? 
    贪心思想: 当前区间只会和res[-1]区间合并. 而一定不会和res[-2]区间合并(按end排序不满足)
    """
    # intervals.sort(key=itemgetter(0))
    res: List[List[int]] = [intervals[0]]
    n = len(intervals)
    for i in range(1, n):
        itv = intervals[i]
        if itv[0] > res[-1][1]:
            res.append(itv)
        elif res[-1][1] < itv[1]:
            res[-1][1] = itv[1]
    return res


def merge_intervals2(intervals: List[List[int]]) -> List[List[int]]:
    """请保证输入的intervals按end有序
    为什么按end排序也行?
    贪心思想: 如果当前区间itv没法合并res[-1]区间, 那一定没法合并res[-1]前的区间. """
    # intervals.sort(key=itemgetter(1))
    res: List[List[int]] = [intervals[0]]
    n = len(intervals)
    for i in range(1, n):
        itv = intervals[i]
        s = itv[0]
        while res and itv[0] <= res[-1][1]:
            s = res.pop()[0]
        if s < itv[0]:
            itv[0] = s
        res.append(itv)
    return res