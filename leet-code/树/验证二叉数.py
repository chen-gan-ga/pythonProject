# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        self.pre = None
        def midorder(root):
            left , right= True , True
            if root.left: left = midorder(root.left)
            if self.pre and self.pre.val >= root.val :#前一个节点的值是否小于当前节点的值
                return False
            self.pre = root#记录前一个节点
            if root.right: right = midorder(root.right)
            return left and right
        return midorder(root)

class Solution0:
    def isValidBST(self, root: TreeNode) -> bool:
        res=[]
        def inOrder(root):
            #终止
            if not root :
                return
            inOrder(root.left)

            res.append(root.val)
            inOrder(root.right)
        inOrder(root)


        for i in range(len(res)-1):
            if res[i]<res[i+1]:pass
            else:return False

        return True

class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        res=[]
        res0=[]
        def inOrder(root):
            #终止
            if not root :
                return
            inOrder(root.left)
            #直接判定
            if res and root.val<=res[-1]:
                res.append(root.val)
                res0.append(-1)
            else:
                res.append(root.val)
            inOrder(root.right)
        inOrder(root)
        if len(res0) >=1 :return False
        else :return True