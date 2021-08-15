# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器。
#
from typing import List


class Solution:
    def __init__(self,nums):
        self.nums=nums

    def sol1(self):
        maxvol=0
        l,r=0,len(self.nums)-1
        while l<r:
            maxvol= max(maxvol,abs(r-l)*min(self.nums[l],self.nums[r]))
            if self.nums[l]<self.nums[r]:
                l=l+1
            elif self.nums[l]>self.nums[r]:
                r=r-1
            else:
                l = l+1
                r = r-1
        return maxvol

num=[1,8,6,2,5,4,8,3,7]
answer=Solution(num)
print(answer.sol1())


#最优
class BestSolution:
    def maxArea(self, height: List[int]) -> int:
        maxvol=0
        l,r=0,len(height)-1
        while l<r:
            cur=min(height[r],height[l])
            maxvol = max(maxvol,cur*(r-l))
            if height[l]<height[r]:
                while height[l]<=cur and l<r:
                    l = l + 1
            elif height[l]>height[r]:
                while height[r] <= cur and l < r:
                    r = r - 1
            else:
                l = l + 1
                r = r - 1
        return maxvol

answer0=BestSolution()
print(answer0.maxArea(num))