# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *


class TrieTreeNode:
    def __init__(self, finish: bool = False) -> None:
        self.finish = finish
        self.children: Dict[str, "TrieTreeNode"] = {}


class Trie:
    def __init__(self) -> None:
        self.root = TrieTreeNode()

    def insert(self, word: str) -> None:
        tn = self.root
        for c in word:
            if c not in tn.children:
                tn.children[c] = TrieTreeNode()
            tn = tn.children[c]
        tn.finish = True

    def search(self, word: str) -> Optional[TrieTreeNode]:
        """
        return: None: 未找到; tn: 可以通过tn.finish判断是匹配word/prefix 
        """
        tn = self.root
        for c in word:
            if c not in tn.children:
                return None
            tn = tn.children[c]
        return tn
