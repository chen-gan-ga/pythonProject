# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
#  
#
# 示例 1：
#
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
#
from typing import List

nums=[9,0,9,8]
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        m=1
        for i in range(len(digits)-1,-1,-1):
            n=n+digits[i]*m
            m=m*10
        n=n+1
        digits=[]
        while n>0:
            l=n%10
            digits.insert(0,l)
            n=n//10
        print(digits)



ans=Solution()
ans.plusOne(nums)
