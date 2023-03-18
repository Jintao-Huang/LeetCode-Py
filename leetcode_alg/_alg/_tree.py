# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *
from .._lc._lc_ds import TreeNode


def _find_path(root: TreeNode, dst: int, path: bytearray) -> bool:
    if root.val == dst:
        return True
    if root.left and _find_path(root.left, dst, path):
        path.append(ord("L"))
        return True
    if root.right and _find_path(root.right, dst, path):
        path.append(ord("R"))
        return True
    return False


def find_path(root: TreeNode, dst: int, path: bytearray) -> None:
    """找从root->(tn.val==dst)的路径."""
    _find_path(root, dst, path)
    path.reverse()


def find_common_ancestor(root: Optional[TreeNode], tn_c: Set[int]) -> Optional[TreeNode]:
    """返回tn_c(treenode children)的公共祖先"""
    if root is None:
        return None
    if root.val in tn_c:
        return root
    ca_l = find_common_ancestor(root.left, tn_c)  # common ancestor left
    ca_r = find_common_ancestor(root.right, tn_c)
    # 分类讨论
    if ca_r is None:
        return ca_l
    elif ca_l is None:
        return ca_r
    else:
        return root


def inorder_traversal(root: TreeNode, res: List[int]) -> None:
    if root.left:
        inorder_traversal(root.left, res)
    res.append(root.val)
    if root.right:
        inorder_traversal(root.right, res)


def level_order_traversal(root: TreeNode) -> List[List[int]]:
    dq = Deque[TreeNode]([root])
    res: List[List[int]] = []
    while dq:
        dq_len = len(dq)
        r: List[int] = []  # sub res
        for _ in range(dq_len):
            tn = dq.popleft()
            r.append(tn.val)
            if tn.left:
                dq.append(tn.left)
            if tn.right:
                dq.append(tn.right)
        res.append(r)
    return res
