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

def printLink(lk):
    while lk:
        print(lk.item,'->',end='')
        lk=lk.next
lk0=creatLink(nums)

shuchu=printLink(lk0)