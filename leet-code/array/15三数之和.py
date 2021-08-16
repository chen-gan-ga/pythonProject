# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#  
#
# 示例 1：
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]

from typing import List
nums = [-2,0,0,2,2]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if(not nums or len(nums)<3):
            return []
        # print(nums)
        res=[]
        for i in range(len(nums)-2):
            if nums[i]>0:break
            if i>0 and nums[i]==nums[i-1]:continue
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    res.append([nums[i],nums[l],nums[r]])
                    while (l < r and nums[l] == nums[l + 1]):
                        l = l + 1
                    while (l < r and nums[r] == nums[r - 1]):
                        r = r - 1
                    l = l + 1
                    r = r - 1
                elif nums[i] + nums[l] + nums[r] > 0 :
                    r = r - 1
                else:
                    l = l + 1

        return res




answer=Solution()
print(answer.threeSum(nums))