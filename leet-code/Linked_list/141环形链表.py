# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        # 快慢指针遍历，性能优化
        h1 = head
        h2 = head
        while h2 and h2.next:
            h1 = h1.next
            h2 = h2.next.next
            if h1 == h2:
                return True
        return False