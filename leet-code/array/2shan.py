class Solution:
    def removeDuplicates(self, nums) -> int:
        i=0
        while i+1 <len(nums):
            if nums[i]==nums[i+1]:
                nums.pop(i+1)
            else: i=i+1
        return nums
nums=[1,1,1,1,1,1,2]
answer=Solution()
print(answer.removeDuplicates(nums))