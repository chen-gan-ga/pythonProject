# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
class Sol(object):
 def moveZeroes(self, nums):
     j=0
     for i in range(len(nums)):
         if nums[i]!= 0:
             nums[i],nums[j]=nums[j],nums[i]
             j=j+1
     return nums
 #哈希
 # def moveZero1(self,nums):
 #     for i in range(len(nums)):




nums=[0,1,0,3,12]

ansewr0=Sol()
print(ansewr0.moveZeroes(nums))



