from leetcode_alg import *
from leetcode_alg.ext import OrderedDict as _OrderedDict


class LRUCache:
    """recommended"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.od = OrderedDict[int, int]()

    def get(self, key: int) -> int:
        if key in self.od:
            v = self.od[key]
            self.od.move_to_end(key)
            return v
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od[key] = value
            self.od.move_to_end(key)
            return
        self.od[key] = value
        if len(self.od) > self.capacity:
            self.od.popitem(last=False)


class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.od = _OrderedDict[int, int]()

    def get(self, key: int) -> int:
        if key in self.od.dict:
            v = self.od.getitem(key)
            self.od.move_to_end(key)
            return v
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.od.dict:
            self.od.setitem(key, value)
            self.od.move_to_end(key)
            return
        self.od.setitem(key, value)
        if len(self.od.dict) > self.capacity:
            self.od.popitem(last=False)


if __name__ == "__main__":
    callable_list = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    args_list = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    print(call_callable_list(callable_list, args_list, globals()))
    callable_list[0] = "LRUCache2"
    print(call_callable_list(callable_list, args_list, globals()))
