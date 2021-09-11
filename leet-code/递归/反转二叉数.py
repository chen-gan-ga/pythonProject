# 翻转一棵二叉树。
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode


    # def isValidBST(self, root: TreeNode) -> bool:
    #     res=[]
    #     def inOrder(root):
    #         #终止
    #         if not root :
    #             return
    #         inOrder(root.left)
    #
    #         res.append(root.val)
    #         inOrder(root.right)
    #     inOrder(root)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def fanzhun(root):
            if not root :
                return
            root.right,root.left=root.left,root.right
            fanzhun()
