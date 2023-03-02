from leetcode_alg import *

if __name__ == "__main__":
    x = [1, 3, 3, 6, 7, 1]
    for sl in [SimpleSortedList(x.copy()), SimpleSortedList2(x.copy(), lambda x: -x)]:
        sl.add(0)
        sl.add(100)
        sl.remove(6)
        print(sl.bisect_left(3))
        print(sl.bisect_right(3))
        print(sl.pop())
        print(sl.ssl)
