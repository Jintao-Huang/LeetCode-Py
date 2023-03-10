
from leetcode_alg import *
import mini_lightning as ml


def func(l: List[int]) -> None:
    n = len(l)
    for i in range(n):
        if i % 2 == 0:
            l[i] = 1


def func2(l: List[int]) -> None:
    l[::2] = [1] * (N // 2)


def func3(l: bytearray) -> None:
    l[::2] = bytearray([1]) * (N // 2)


if __name__ == "__main__":
    N = 100000
    x = [0] * N
    ml.test_time(lambda: func(x), 10)
    print(sum(x))
    x = [0] * N
    ml.test_time(lambda: func2(x), 10)
    print(sum(x))
    x = bytearray(N)
    ml.test_time(lambda: func3(x), 10)
    ml.test_time(lambda: [0] * N, 10)
    ml.test_time(lambda: bytearray([0]) * N, 10)
    print(sum(x))
    """
    [INFO: mini-lightning] time[number=10]: 0.003052±0.000063, max=0.003151, min=0.002972
    [INFO: mini-lightning] time[number=10]: 0.000253±0.000037, max=0.000356, min=0.000218
    [INFO: mini-lightning] time[number=10]: 0.000014±0.000002, max=0.000020, min=0.000013 
    [INFO: mini-lightning] time[number=10]: 0.000159±0.000046, max=0.000189, min=0.000026
    [INFO: mini-lightning] time[number=10]: 0.000002±0.000000, max=0.000003, min=0.000001   
    """


if __name__ == "__main__":
    # 浅copy
    x = [1, 2, 3, 4, 5]
    y = x[:]
    y[0] = 100
    print(x)
    # 
    y = x[:3]
    y[0] = 100
    print(x)