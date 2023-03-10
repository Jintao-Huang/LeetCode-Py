# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:


from .._types import *


def build_nextval(p: str) -> List[int]:
    n = len(p)
    if n == 0:
        return []
    nextval = [0]  # 省略-1
    j = 0
    for i in range(1, n):
        c = p[i]
        # nextval
        nv = nextval[-1]
        if nv > 0 and c == p[nv]:
            nextval[-1] = nextval[nv-1]
        #
        while j > 0 and p[j] != c:
            j = nextval[j-1]
        if p[j] == c:
            j += 1
        nextval.append(j)
    return nextval


def kmp(s: str, p: str) -> int:
    """只匹配第一个(可以改造成匹配所有的匹配). p: pattern. 
    ref: 算法导论"""
    m = len(p)
    nextval = build_nextval(p)
    j = 0  # p[j], nextval[j]
    for i, c in enumerate(s):
        while j > 0 and p[j] != c:
            j = nextval[j-1]  # 跳转到应该继续匹配的位置
        if p[j] == c:
            j += 1
        #
        if j == m:
            return i-m+1
    return -1
