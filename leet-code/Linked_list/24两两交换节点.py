# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def creatLink(nums):
    head=ListNode(nums[0])
    temp=head
    for i in range(1,len(nums)):
        temp.next=ListNode(nums[i])
        temp=temp.next
    return head

nums=[1,2,3,4]
head0=creatLink(nums)

class Solution:
    def swapPairs(self, head) :
        hakehead=ListNode()
        hakehead.next=head
        temp=hakehead

        while temp.next and temp.next.next:
            #初始化需要交换的两位
            do1,do2=temp.next,temp.next.next
            #执行交换
            temp.next = do2
            do1.next,do2.next=do2.next,do1
            #初始化下一组
            temp=do1
        return hakehead.next


answer=Solution()
print(answer.swapPairs(head0).val)
