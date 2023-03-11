from operator import add, mul, lt, gt, le, ge, neg, itemgetter
from heapq import (
    heapify, heappop, heappush, heappushpop, heapreplace,  # C
    merge as merge_heapq, nlargest, nsmallest  # py
)
from bisect import bisect_left, bisect_right, insort_left, insort_right  # C
from math import (  # C
    sqrt, log2, floor, trunc, ceil, gcd, lcm, factorial, comb, perm, prod,
    isclose, dist as dist_math, hypot, 
)
from random import randint
from functools import partial, cache, lru_cache, cmp_to_key, reduce  # C
from itertools import accumulate, chain  # C
# from collections import deque, namedtuple, defaultdict, Counter  # use typing
from copy import copy, deepcopy  # C
from typing import (
    Literal, List, Tuple, Dict, Set, Callable, Optional, Union, Any,
    Deque, NamedTuple, DefaultDict, Counter, OrderedDict,   # C
    Sequence, Mapping, Iterable, Iterator, TypeVar, Generic
)
from enum import Enum
from sortedcontainers import SortedList, SortedDict, SortedSet, SortedKeyList  # py
#
INF = int(1e18)  # long long: [-9223372036854775808, 9223372036854775807]
