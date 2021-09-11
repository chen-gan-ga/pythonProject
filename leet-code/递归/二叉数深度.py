# 如果我们知道了左子树和右子树的最大深度 ll 和 rr，那么该二叉树的最大深度即为
#
# max(l,r) + 1
# 可循环此步


class Solution(object):
    def maxDepth(self, root):

        if root == None:
            return 0

        left_high = self.maxDepth(root.left)
        right_high = self.maxDepth(root.right)

        return max(left_high, right_high) + 1






