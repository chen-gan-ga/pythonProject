# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]

class Node:
    def __init__ (self,item):
        self.item=item
        self.next=None



nums=[0,1,2,3,4,5]
def creatLink(nums):
    head=Node(nums[0])
    temp=head
    for i in range(1,len(nums)):
        temp.next=Node(nums[i])
        temp=temp.next
    return head


head = [1,2,3,4,5]
lk0=creatLink(head)


class Solution:
    def reverseList0(self, head: Node) -> Node:
        # 遍历link,将元素存入数组
        nums=[]
        while head:
            nums.append(head.item)
            head=head.next
        print(nums)

        head0=Node(nums[len(nums)-1])
        temp=head0
        for i in range(len(nums)-2,-1,-1):
            temp.next=Node(nums[1])
            temp=temp.next
        return head0
    #迭代
    def reverseList(self, head: Node) -> Node:
        done,do=None,head
        while do :
            will=do.next
            do.next=done
            done=do
            do=will
        return done
    #递归
    def reverseListo(self,head:Node)-> Node:
        if not head or head.next == None: return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res




answer=Solution()
print(answer.reverseList0(lk0).next.item)



