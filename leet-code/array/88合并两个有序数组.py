# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
#
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
#
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
#
#  
#
# 示例 1：
#
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
from typing import List
nums1 = [0]
m = 0
nums2 = [6]
n = 1

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        #还是快慢指针
        i,j=0,0
        while nums2 and nums1:
            if nums1[i]<nums2[j] and nums1[i]!=0:
                i=i+1
            elif nums1[i]>=nums2[j] :
                nums1.insert(i,nums2[j])
                nums1.pop(len(nums1)-1)
                nums2.pop(0)
            elif nums1[i]==0:
                nums1.pop(i)
                nums1.insert(i,nums2[0])
                nums2.pop(0)
                i = i + 1
        nums1.sort



    def merge0(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
            nums1.pop(m)
        nums1.sort()
answer=Solution()
print(answer.merge(nums1,m,nums2,n))

