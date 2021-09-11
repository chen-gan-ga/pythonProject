class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1 or num==0:return True
        left,right=1,num
        while left<=right:
            mid=(left+right)//2
            if mid*mid==num:return True
            elif mid**2 <num and (mid+1)**2>num:return False
            elif mid*mid<num:left=mid+1
            else:right=mid-1