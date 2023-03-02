from leetcode_alg import *


if __name__ == "__main__":
    bit2 = BinaryIndexedTree2([1, 2, 3, 4, 5])
    print(bit2.query_range(0, 4))  # 15
    bit2.update_range(0, 3, 1)  
    print(bit2.query_range(0, 4))  # 19


if __name__ == "__main__":
    bit2 = SegmentTree2([1, 2, 3, 4, 5])
    print(bit2.query_range(0, 4))  # 15
    bit2.update_range(0, 3, 1)  
    print(bit2.query_range(0, 4))  # 19