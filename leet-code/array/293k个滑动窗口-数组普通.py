# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
#  
#
# 示例 1：
#
# 输入：
from typing import List
import collections
# 输出：[3,3,5,5,6,7]
nums = [1,3,-1,-3,5,3,6,7]
k=3
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for i in range(len(nums)-k+1):
            res.append(max([ nums[i] for i in range(i,i+k)]))
        return res
    def maxSlidingWindowCx(self, nums: List[int], k: int) -> List[int]:
        #初始化一个双端队列,并限制其长度
        queue=collections.deque(maxlen=k )
        #将前k加进去
        for i in range(k):
            queue.append(nums[i])
        res=[max(queue)]
        for i in range(k,len(nums)):
            queue.append(nums[i])
            res.append(max(queue))
        return res
        #问题计算max

    def maxSlidingWindowBest(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dq = collections.deque()

        for i in range(len(nums)):
            # 只要当前遍历的元素的值比队尾大，让队尾出队列，
            # 最终队列中的最小元素是大于当前元素的
            while dq and dq[-1] < nums[i]:
                dq.pop()
            # 当前遍历的元素入队列， 此时队列中的元素一定是有序的，队列头部最大
            dq.append(nums[i])
            if i >= k - 1:
                # 如果窗口即将失效（下一次循环要失效）的值与当前对列头部的值相同，那么将对头的值出队列，
                # 注意只pop一次，可能两个4，相邻同时是最大值，
                ans.append(dq[0])
                # 从队列中删除即将失效的数据
                if nums[i - k + 1] == dq[0]:
                    dq.popleft()
        return ans
answer=Solution()
print(answer.maxSlidingWindowCx(nums,k))




