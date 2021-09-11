from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #保存节点值
        result = []
        #后序遍历
        def pre_order(root):
            #跟节点非空入队列递归遍历
            if root:
                #递归遍历
                for node in root.children:
                    pre_order(node)
                #节点值入队列
                result.append(root.val)
        pre_order(root)
        return result

