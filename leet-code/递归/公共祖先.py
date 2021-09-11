# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        # 边界条件，如果匹配到left或right就直接返回停止递归
        if root.val == p.val or root.val == q.val:
            return root
        # 这两行代码可以无脑先写好！
        # 因为是DFS算法，这个模板可以无脑套用，写上之后可能你思路就清晰很多
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果既在左子树找到，又在右子树找到，那么毫无疑问当前root就是公共节点
        if left and right:
            return root
        # 只有左子树有，那么直接返回左子树匹配到的第一个节点
        if left:
            return left
        if right:
            return right

