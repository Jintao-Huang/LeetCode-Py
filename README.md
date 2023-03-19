# LeetCode-Py
[![Python Version](https://img.shields.io/pypi/pyversions/leetcode-alg)](https://pypi.org/project/leetcode-alg/)
[![PyPI Status](https://badge.fury.io/py/leetcode-alg.svg)](https://badge.fury.io/py/leetcode-alg)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/Jintao-Huang/LeetCode-Py/blob/main/LICENSE)


## 介绍
1. `LeetCode-Py`仓库中包含2大内容. (**持续更新中**)
   1. 包含大量leetcode(python)题目的解答(将会收集**1k题**以上, 目前处于开发中). 
   2. 算法库: `leetcode-alg`. 
2. `LeetCode-Py`的**习题解答的风格**是在最优复杂度的前提下, 写出最简洁的代码(**不做过多细节的优化**: 因为不同于c/c++, python容易反向优化). 旨在将**最优雅**的python代码放入`answer/`文件夹内. 
3. `leetcode-alg`是针对leetcode解题的数据结构和算法库, 其**设计准则**是: 以通用性为核心, 并以最大可能进行性能优化. 


## 性能和功能
1. `answer/`中**time击败**: (不使用trick)
   1. 100%: 1, 11, 16, 18, 39, 42, 57, 72, 84, 85, 146, 167, 200, 300, 354, 416, 435, 518, 1143, 1349, 2096, 2171, 2203
   2. 95%: 2, 28, 40, 51, 52, 56, 102, 107, 112, 113, 124, 153, 204, 207, 210, 239, 307, 322, 454, 496, 503, 704, 875, 1044, o51
   3. 85%: 4, 15, 19, 92, 208, 215, 876, 1584, o40
   4. 60%: 
   5. 其他: 
2. 已有的功能: (持续更新中)
   1. 算法: 
      1. array: unique, partition, partition2, merge, merge2, diff, quick_select, two_sum
      2. dp: LIS, LIS2, LCS, LCS2, LCS3, edit_distance, matrix_chain, matrix_chain2
      3. graph: dijkstra, dijkstra2, dijkstra3, kruskal, prim, prim2, topo_sort, Dinic, hungarian
      4. greed: merge_intervals, merge_intervals2
      5. knapsack: knapsack, knapsackV, knapsack_C, knapsackV_C
      6. linkedlist: reverse_list, find_mid_node, find_last_kth_node
      7. math: is_prime, find_primes
      8. monotone_deque: monotone_deque, monotone_deque2
      9. monotone_stack: monotone_stack, monotone_stack2, monotone_stack3, largest_rect, largest_rect2
      10. search: lower_bound, upper_bound, n_queens
      11. string: build_nextval, kmp
      12. tree: find_path, find_common_ancestor, inorder_traversal, level_order_traversal
      13. unimportant: 
          1. array: reverse, euclidean_dist, manhattan_dist, prefix_sum
          2. bisect: bisect_left, bisect_right, binary_search
          3. math: gcd, lcm, fast_pow
          4. random: randperm
          5. sort: quick_sort, merge_sort, heap_sort, heap_sort2
   2. 数据结构:
      1. binary_indexed_tree: BinaryIndexedTree, BinaryIndexedTree2
      2. heap: Heap, Heap2
      3. linkedlist: LinkedListNode, LinkedList
      4. segment_tree: SegmentTree, SegmentTree2
      5. sorted_list: SimpleSortedList
      6. string_hasher: StringHasher, StringHasher2
      7. trie: TrieTreeNode, Trie
      8. union_find: UnionFind
      9. unimportant: 
         1. ordered_dict: OrderedDict
   3. LeetCode Tools:
      1. 数据结构: ListNode, TreeNode
      2. tools: to_linkedlist, from_linkedlist, to_tree, from_tree, call_callable_list
3. todo
   1. 算法: 
      1. monotone_deque: next_ge_k_len, prev_le_k_len
      2. monotone_stack: next_ge_min
      3. string_op: string_add, string_mul
      4. tree: bst_min, bst_max
      5. unimportant: 
         1. math: int2str, prime_factor, BigInteger
   2. 数据结构: 
      1. extension: BBST, HuffmanTree, RBTree




## 安装和使用
1. 安装: 
    ```bash
    # (推荐)将此仓库下载的本地, 进入setup.py所在目录, 输入以下命令
    pip install .
    # or 从pypi下载
    pip install leetcode-alg -U
    ```
    
2. 使用: 例子可以查看`answer/`
   ```python
   from leetcode_alg import *
   # if you want to import additional features
   from leetcode_alg.ext import *
   ```



## 索引
### 数据结构
1. 线段树: 307
   1. Lazy: 
   2. 离散化: o51
   3. -(易混淆): 2021
2. 树状数组: 307
   1. 变体: 
   2. 离散化: o51
3. SortedList: o51
4. 哈希表: 1143, 2183, 416
   1. N数: 1, 15, 454
5. 链表: 
   1. 前向链表: 2, 19, 21, 23, 24, 25, 92, 876, 2181
   2. 双向循环链表: OrderedDict
6. 单调栈/队列
   1. 单调栈: 496, 503
      1. 双向: 42, 84, 85
   2. 单调队列: 239
7. 前缀树(Trie): 208
   1. -(易混淆): 14
8. 栈: 20
9. 堆: 23, 215, o40
   1. 可动态修改的堆(Heap2): dijkstra, prim
10. UnionFind: kruskal, 200
11. OrderedDict: 146(LRU)




### 算法
1. 分治法: 
   1. 2路: 常见2路递归(merge sort, quick_sort, 树的dfs等), 23
2. 二分查找: 
   1. 自己设计cond: 
      1. lower_bound: 4, 153, 875
      2. upper_bound: 
   2. 直接调用bisect: 704
      1. LIS: 300, 354, 435(非递减), 1143(LCS)
3. 滑动窗口: 3
4. 搜索:
   1. 链: 
      1. 回溯: 17, 22, 39, 40, 51, 52
   2. 树: 
      1. 回溯: 113
      2. dfs: 112, 124
         1. 公共祖先: 2096
         2. 递归模式dfs: 112
      3. bfs: 102, 107
   3. 图: 
      1. dfs: 200
      2. bfs: 200
5. 图算法: 
   1. dijkstra: 2203(重边的处理)
   2. kruskal(稀疏图): 1584
   3. prim(稠密图): 1584
   4. 拓扑排序: 207, 210
   5. dinic: 1349
   6. 匈牙利算法: 1349
6. DP(or memo-dfs): 
   1. nums\[i..j\]: 5
   2. nums\[..i\]: 300, 435
   3. s\[..i\], s\[..j\]: 72, 1143
   4. 双dp: 42, 2167
   5. 背包: 39, 322, 416, 518
7. 双指针: 11, 42
   1. N数: 15, 16, 18, 167
8. 贪心: 11, 12, 42, 2037, 2038, 2182
   1. 区间贪心: 56, 57, 435
9. 位运算: 2166
10. 字符串: 
    1. 字符串哈希: 28, 1044
    2. kmp: 28



#### 其他 
1. 中心法: 双向单调栈, 5, 2171, 2203
2. 去重: 
   1. N数: 15, 16, 18
3. 排序: 离散化, kruskal, 2171
   1. N数: 同双指针N数
   2. map有序化: 2021, 2165, 2170, 2183
   3. with贪心: 区间贪心, 2037
      1. -(非显式的sort): 12, 2182
4. int溢出: 7, 8
5. 分类讨论: 
   1. 次大/小: 2170, 2182
      1. 不以0开头: 7, 8, 2165
   2. 其他: 线段树的query_range, 4, find_common_ancestor(2096)
6. 随机算法: 215, o40, quick_sort
7. 数学: 
   1. gcd: 2183
   2. 质数: 204
8. 日期: 




### 未分类 
1. 暴力: 2180
2. 过于简单: 2022, 2164, 2169
3. 6, 9, 13, 2043

