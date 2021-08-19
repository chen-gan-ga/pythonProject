# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        hakehead = ListNode()
        temp=hakehead
        # 注意判断列表非空 不是判断val
        while l1 and l2:
            if l1.val<l2.val:
                temp.next=l1
                temp=temp.next
                l1=l1.next
            elif l1.val>=l2.val:
                temp.next = l2
                temp=temp.next
                l2=l2.next
        #三元表达式
        temp.next=l1 if l1 else l2
        return hakehead.next



