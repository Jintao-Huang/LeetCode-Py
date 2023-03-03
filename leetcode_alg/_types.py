from heapq import (
    heapify, heappop, heappush, heappushpop, heapreplace,  # C
    merge as heapq_merge, nlargest, nsmallest  # py
)
from bisect import bisect_left, bisect_right, insort_left, insort_right  # C
from math import (  # C
    sqrt, log2, floor, trunc, ceil, gcd, lcm, factorial, comb, perm, prod
)
from random import randint
from functools import partial, cache, lru_cache, cmp_to_key
# from collections import deque, namedtuple, defaultdict, Counter  # use typing
from copy import copy, deepcopy
from typing import (
    Literal, List, Tuple, Dict, Set, Callable, Optional, Union, Any,
    Deque, NamedTuple, DefaultDict, Counter,
    Sequence, Mapping, Iterable, Iterator,
)
from enum import Enum
from sortedcontainers import SortedList, SortedDict, SortedSet, SortedKeyList  # py
#
