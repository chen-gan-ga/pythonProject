from typing import List

# 33. 搜索旋转排序数组
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            if target==nums[l]:
                return l
            if target==nums[r]:
                return r
            #mid在前半部分有序
            if nums[mid]>=nums[l]:
                #目标也在有序的前部分
                if target>nums[l] and target<nums[mid]:
                    l1=l
                    r1=mid
                    while  l1<=r1:
                        mid1=(l1+r1)//2
                        if nums[mid1]==target: return mid1
                        elif nums[mid1]>target:
                            r1=mid1-1
                        else:
                            l1=mid1+1
                    return -1
                else:l=mid+1
            else :
                if target<nums[r] and target>nums[mid]:
                    l2=mid
                    r2=r
                    while l2<=r2:
                        mid2=(l2+r2)//2
                        if nums[mid2]==target:return mid2
                        elif nums[mid2]>target:
                            r2=mid2-1
                        else:
                            l2=mid2+1
                    return -1
                else:r=mid-1
        return -1
nums = [8,1,2,3,4,5,6,7]
target = 6
ans=Solution()
print(ans.search(nums,target))




