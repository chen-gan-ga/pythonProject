#定义树
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left,self.right=None,None
#遍历方式：
#1.前序（Pre-order）：根-左-右
#2.中序（In-order）：左-根-右
#3.后序（Post-order）:左-右-根

    def preOrder(self,root):
        self.traverse_path.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
    def inOrder(self,root):
        self.inOrder(root.left)
        self.traverse_path.append(root.val)
        self.inOrder(root.right)
    def postOrder(self,root):
        self.postOrder(root.left)
        self.postOrder(root.right)
        self.traverse_path.append(root.val)
# https://visualgo.net/zh/bst


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 前序递归
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        # # 中序递归
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        # # 后序递归
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


