# LeetCode-Py
[![Python Version](https://img.shields.io/pypi/pyversions/leetcode-alg)](https://pypi.org/project/leetcode-alg/)
[![PyPI Status](https://badge.fury.io/py/leetcode-alg.svg)](https://badge.fury.io/py/leetcode-alg)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/Jintao-Huang/LeetCode-Py/blob/main/LICENSE)


## 介绍
1. `LeetCode-Py`仓库中包含2大内容. 
   1. 包含大量leetcode(python)题目的解答(将会收集**1k题**以上, 目前处于开发中). 
   2. 算法库: `leetcode-alg`. 
2. `LeetCode-Py`的**习题解答的风格**是在最优复杂度的前提下, 写出最简洁的代码(**不做过多细节的优化**: 因为不同于c/c++, python容易反向优化). 旨在将最优雅的python代码放入`answer`文件夹内. 
3. `leetcode-alg`是针对leetcode解题的数据结构和算法库, 其**设计准则**是: 以通用性为核心, 并以最大可能进行性能优化. 


## 安装和使用
1. 安装: 
    ```bash
    # (推荐)将此仓库下载的本地, 进入setup.py所在目录, 输入以下命令
    pip install .
    # or 从pypi下载
    pip install leetcode-alg -U
    ```
    
2. 使用: `from leetcode_alg import *`

3. 已有的功能(持续更新中)
   1. 算法: 
      1. array: unique, partition, partition2, merge, merge2, diff, find_kth_smallest
      2. graph: dijkstra, dijkstra2, kruskal, prim, prim2
      3. search: lower_bound, upper_bound
      4. tree: find_path, find_common_ancestor
      5. unimportant: 
         1. array: reverse, euclidean_dist, manhattan_dist, prefix_sum
         2. bisect: bisect_left, bisect_right, binary_search
         3. math: gcd, lcm
         4. random: randperm
         5. sort: quick_sort, merge_sort, heap_sort, heap_sort2
   2. 数据结构:
      1. binary_indexed_tree: BinaryIndexedTree, BinaryIndexedTree2
      2. heap: Heap, Heap2
      3. segment_tree: SegmentTree, SegmentTree2
      4. sorted_list: SimpleSortedList
      5. union_find: UnionFind
   3. LeetCode Tools:
      1. 数据结构: ListNode, TreeNode
      2. tools: to_linkedlist, from_linkedlist, to_tree, from_tree, call_callable_list
   
4. todo
   1. 算法: 
      1. dp: LIS, LIS2, LCS, LCS2, edit_distance, matrix_chain, matrix_chain2
      2. graph: Dinic, dinic, hungarian, topo_sort
      3. knapsack: k01, k01_full_max, k01_full_min, kC, kC_full_max, kC_full_min, kC2, kC_full_max2, kC_full_min2, kC_full_cnt
      4. linkedlist: find_mid_node, reverse_list, find_last_nth_node
      5. math: fast_pow, find_prime_nums
      6. monotone_deque: next_k_max, prev_k_max, next_k_min, next_ge_k_len, prev_le_k_len
      7. monotone_stack: next_gt, prev_gt, next_lt, prev_lt, next_ge, next_gt2, next_ge_prev_gt, next_ge_min, largest_rect
      8. search: n_queens
      9. string_op: string_add, string_mul
      10. string: kmp, kmp2, is_palindromic
      11. tree: bst_min, bst_max, preorder_traversal, inorder_traversal, postorder_traversal
   2. 数据结构: 
      1. linkedlist: LinkedList
      2. string_hasher: StringHasher
      3. trie: Trie
      4. extension: bbst, huffman, rb_tree
      5. unimportant: ordered_dict




## 索引
### 数据结构
1. 线段树: 307
   1. lazy: 
   2. 离散化: o51
   3. -(易混淆): 2021
2. 树状数组: 307
   1. 变体: 
   2. 离散化: o51
3. sorted list: o51
4. 哈希表: 1, 2183
5. 链表: 
   1. 前向链表: 2, 19, 21, 23, 24, 25, 2181
   2. 双向循环链表: 
6. 单调栈/队列
   1. 单调栈: 
   2. 单调队列: 
7. 前缀树(Trie): 
   1. -(易混淆): 14
8. 栈: 20
9. 堆: 23, 215
   1. 可动态修改的堆: 
      1. with dijkstra, prim: always
10. union find
    1. with kruskal: always




### 算法
1. 分治法: 
   1. 2路: 常见2路递归(merge sort, quick_sort, 树的dfs等), 23
2. 二分查找: 4
3. 滑动窗口: 3
4. 图的搜索:
   1. 回溯: 17, 22
   2. dfs:
   3. bfs: 
5. 树的搜索
   1. dfs: 
      1. 公共祖先: 2096
   2. bfs: 
6. 图算法: 
   1. dijkstra: 2203(重边的处理)
   2. kruskal(稀疏图): 1584
   3. prim(稠密图): 1584
   4. dinic: 
   5. 匈牙利算法: 
7. DP
   1. \[i..j\]dp: 5
   2. 双向dp: 2167
8. 双指针: 11
   1. N数: 15, 16, 18
9. 贪心: 11, 12, 2037, 2038, 2182
10. 位运算: 2166, 



#### 其他 
1. 中心法: 5, 2171, 2203
2. 去重: 
   1. N数: 15, 16, 18
3. 排序: 
   1. N数: 同双指针N数
   2. map有序化: 2021, 2165, 2170, 2183
   3. with贪心: 2037
      1. -(暗含): 12, 2182
   4. with离散化, kruskal: always
   5. 2171
4. int溢出: 7, 8
5. 分类讨论
   1. 次大/小: 2170, 2182
      1. 不以0开头: 7, 8, 2165
   2. 其他: 线段树的query_range, 4, find_common_ancestor(2096)
6. 随机算法: 215, quick_sort
7. 数学: 
   1. gcd: 2183
   2. 质数: 
8. 日期: 




### 未分类 
1. 暴力: 2180
2. 过于简单: 2022, 2164, 2169
3. 6, 9, 13, 2043

