class Solution0(object):
    def inorderTraversal(self, root):
        res = []

        def dfs(root):
            if not root:
                return
            # 按照 左-打印-右的方式遍历
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res
# 题目要求的是中序遍历，那就按照 左-打印-右这种顺序遍历树就可以了，递归函数实现
#
# 终止条件：当前节点为空时
# 函数内：递归的调用左节点，打印当前节点，再递归调用右节点
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import List


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]

        def inOrder(root):
            #终止
            if not root :
                return
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return res

