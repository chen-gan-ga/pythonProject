from typing import List
nums = [2,2,3,2]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]=dic[nums[i]]+1
            else:dic[nums[i]]=1
            for key in dic:
                if dic[key]==1:return key
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] != nums[i] and nums[i-1] !=nums[i]:return nums[i]
        return nums[-1]

ans=Solution1()
print(ans.singleNumber(nums))