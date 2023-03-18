# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *

"""
01背包
    普通的01背包, capacity无需装满: 
        knapsack(is_01=True, max_min=max, fill_capacity=False, init_value=0)
    最大化装满01背包: 
        knapsack(is_01=True, max_min=max, fill_capacity=True, init_value=-INF)
            or init_value=-1(如果所有的choices[i]>0)
    最小化装满01背包: 
        knapsack(is_01=True, max_min=min, fill_capacity=True, init_value=INF)
完全背包: 
    普通的01背包, capacity无需装满: 
        knapsack(is_01=False, max_min=max, fill_capacity=False, init_value=0)
    最大化装满01背包: 
        knapsack(is_01=False, max_min=max, fill_capacity=True, init_value=-INF)
            or init_value=-1(如果所有的choices[i]>0)
    最小化装满01背包: 
        knapsack(is_01=False, max_min=min, fill_capacity=True, init_value=INF)
"""

_func_mapper = {
    "max": gt,
    "min": lt
}


def knapsack(choices: List[int], capacity: int,
             is_01: bool, max_min: Literal["max", "min"],
             fill_capacity: bool, init_value: int) -> int:
    """value=1"""
    dp = [init_value] * (capacity+1)
    dp[0] = 0
    _comp = _func_mapper[max_min]
    not_fc = not fill_capacity
    #
    for c in choices:
        _iter = range(c, capacity+1)
        if is_01:
            _iter = reversed(_iter)
        for capa in _iter:
            c2 = capa-c
            if not_fc or dp[c2] != init_value and _comp(dp[c2] + 1, dp[capa]):  # max: gt, min: lt
                dp[capa] = dp[c2] + 1
    return dp[capacity]


def knapsackV(choices: List[int], capacity: int, values: List[int],
              is_01: bool, max_min: Literal["max", "min"],
              fill_capacity: bool, init_value: int) -> int:
    dp = [init_value] * (capacity+1)
    dp[0] = 0
    _comp = _func_mapper[max_min]
    not_fc = not fill_capacity
    #
    for c, v in zip(choices, values):
        _iter = range(c, capacity+1)
        if is_01:
            _iter = reversed(_iter)
        for capa in _iter:
            c2 = capa-c
            if not_fc or dp[c2] != init_value and _comp(dp[c2] + v, dp[capa]):
                dp[capa] = dp[c2] + v
    return dp[capacity]


def knapsack_C(choices: List[int], capacity: int,
               max_min: Literal["max", "min"],
               fill_capacity: bool, init_value: int) -> int:
    """value=1. 完全背包的另一实现. (slower than knapsack)"""
    dp = [init_value] * (capacity+1)
    dp[0] = 0
    _comp = _func_mapper[max_min]
    not_fc = not fill_capacity
    #
    for capa in range(capacity+1):
        for c in choices:
            c2 = capa-c
            if c2 >= 0 and (not_fc or dp[c2] != init_value) and _comp(dp[c2]+1, dp[capa]):
                dp[capa] = dp[c2] + 1
    return dp[capacity]


def knapsackV_C(choices: List[int], capacity: int, values: List[int],
                max_min: Literal["max", "min"],
                fill_capacity: bool, init_value: int) -> int:
    dp = [init_value] * (capacity+1)
    dp[0] = 0
    _comp = _func_mapper[max_min]
    not_fc = not fill_capacity
    #
    for capa in range(capacity+1):
        for c, v in zip(choices, values):
            c2 = capa-c
            if c2 >= 0 and (not_fc or dp[c2] != init_value) and _comp(dp[c2]+v, dp[capa]):
                dp[capa] = dp[c2] + v
    return dp[capacity]
