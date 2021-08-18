# 假设链表环前有 aa 个节点，环内有 bb 个节点
# 本题核心思路：走 a+nba+nb 步一定处于环的入口位置
#
# 利用快慢指针 fastfast 和 slowslow，fastfast 一次走两步，slowslow 一次走一步
# 当两个指针第一次相遇时，假设 slowslow 走了 ss 步，下面计算 fastfast 走过的步数
# i. fastfast 比 slowslow 多走了 nn 个环：f = s + nbf=s+nb
# ii. fastfast 比 slowslow 多走一倍的步数：f = 2sf=2s --> 跟上式联立可得 s = nbs=nb
# iii. 综上计算得，f = 2nbf=2nb，s = nbs=nb
# 也就是两个指针第一次相遇时，都走过了环的倍数，那么再走 aa 步就可以到达环的入口
# 让 fastfast 从头再走，slowslow 留在原地，fastfast 和 slowslow 均一次走一步，当两个指针第二次相遇时，fastfast 走了 aa 步，slowslow 走了 a+nba+nb 步
# 此时 slowslow 就在环的入口处，返回 slowslow
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break;
        fast = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow
# 方法一：哈希表
# 思路与算法
#
# 一个非常直观的思路是：我们遍历链表中的每个节点，并将它记录下来；一旦遇到了此前遍历过的节点，就可以判定链表中存在环。借助哈希表可以很方便地实现。
