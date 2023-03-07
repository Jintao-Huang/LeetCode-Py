# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:
"""
01背包
    普通的01背包, capacity无需装满: 
        is_01=True, max_min=max, fill_capacity=False, init_value=0
    最大化装满01背包: 
        is_01=True, max_min=max, fill_capacity=True, init_value=-1(if choices[i]>0) else -INF
    最小化装满01背包: 
        is_01=True, max_min=min, fill_capacity=True, init_value=INF
完全背包: 
    普通的01背包, capacity无需装满: 
        is_01=False, max_min=max, fill_capacity=False, init_value=0
    最大化装满01背包: 
        is_01=False, max_min=max, fill_capacity=True, init_value=-1(if choices[i]>0) else -INF
    最小化装满01背包: 
        is_01=False, max_min=min, fill_capacity=True, init_value=INF
"""
from .._types import *

_func_mapper = {
    "max": max,
    "min": min
}


def knapsack(choices: List[int], capacity: int,
             is_01: bool, max_min: Literal["max", "min"],
             fill_capacity: bool, init_value: int) -> int:
    """value=1"""
    dp = [init_value] * (capacity+1)
    dp[0] = 0
    _max_min_func = _func_mapper[max_min]
    #
    for c in choices:
        _iter = range(c, capacity+1)
        if is_01:
            _iter = reversed(_iter)
        for capa in _iter:
            c2 = capa-c
            if fill_capacity and dp[c2] == init_value:
                continue
            dp[capa] = _max_min_func(dp[capa], dp[c2] + 1)
    return dp[capacity]


def knapsackV(choices: List[int], capacity: int, values: List[int],
              is_01: bool, max_min: Literal["max", "min"],
              fill_capacity: bool, init_value: int) -> int:
    dp = [init_value] * (capacity+1)
    dp[0] = 0
    _max_min_func = _func_mapper[max_min]
    #
    for c, v in zip(choices, values):
        _iter = range(c, capacity+1)
        if is_01:
            _iter = reversed(_iter)
        for capa in _iter:
            c2 = capa-c
            if fill_capacity and dp[c2] == init_value:
                continue
            dp[capa] = _max_min_func(dp[capa], dp[c2] + v)
    return dp[capacity]


def knapsack_C(choices: List[int], capacity: int,
               max_min: Literal["max", "min"],
               fill_capacity: bool, init_value: int) -> int:
    """value=1. 完全背包的另一实现. (slower)"""
    dp = [init_value] * (capacity+1)
    dp[0] = 0
    _max_min_func = _func_mapper[max_min]
    #
    for capa in range(capacity+1):
        for c in choices:
            c2 = capa-c
            if c2 >= 0:
                if fill_capacity and dp[c2] == init_value:
                    continue
                dp[capa] = _max_min_func(dp[capa], dp[c2] + 1)
    return dp[capacity]


def knapsackV_C(choices: List[int], capacity: int, values: List[int],
                max_min: Literal["max", "min"],
                fill_capacity: bool, init_value: int) -> int:
    dp = [init_value] * (capacity+1)
    dp[0] = 0
    _max_min_func = _func_mapper[max_min]
    #
    for capa in range(capacity+1):
        for c, v in zip(choices, values):
            c2 = capa-c
            if c2 >= 0:
                if fill_capacity and dp[c2] == init_value:
                    continue
                dp[capa] = _max_min_func(dp[capa], dp[c2] + v)
    return dp[capacity]
