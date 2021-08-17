class Node:
    def __init__ (self,item):
        self.item=item
        self.next=None

# a=Node(1)
# b=Node(2)
# c=Node(3)
# a.next=b
# b.next=c
# c.next=ad
def tailInsert(nums:list):
    #实例化头部与尾部
    head=Node(nums[0])
    tail=Node(nums[1])
    head.next = tail
    #遍历nums数组，依次从头部插入链表
    for i in range(2,len(nums)):
        node=Node(nums[i])
        tail.next=node
        tail=node
    return head

def headInsert(nums:list):
    #定义链表头部
    head=Node(nums[0])
    #遍历nums数组，依次从头部插入链表
    for i in range(1,len(nums)):
        #将新元素实例化为新node
        node=Node(nums[i])
        #将node指向head
        node.next=head
        #将node改为头部
        head = node
    return head

def printLink(lk):
    while lk:
        print(lk.item,'->',end='')
        lk=lk.next

nums=[1,2,3]
#将nums调用headInsert函数变成列表
lk0=headInsert(nums)
lk1=tailInsert(nums)
# print(lk0.next.item)
# 掉用printLink函数 遍历列表
# printLink(lk0)
# print('')
# printLink(lk1)
#

print(printLink(lk0))

