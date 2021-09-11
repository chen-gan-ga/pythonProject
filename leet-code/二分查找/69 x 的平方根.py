# 给你一个非负整数 x ，计算并返回 x 的 平方根 。
#
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
x=8
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1 or x==0:return x
        left,right=1,x
        while left<=right:
            mid=(left+right)//2
            if mid*mid==x:return mid
            #mid**2 <=x and (mid+1)**2>x:
            elif mid*mid<x:left=mid+1
            else:right=mid-1
        return right

ans=Solution()
print(ans.mySqrt(x))