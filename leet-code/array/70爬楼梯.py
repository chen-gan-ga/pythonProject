class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n== 2 :return n
        f1,f2=1,2
        for i in range(3,n+1):
            num=f1+f2
            f1=f2
            f2=num
        return num
    def climbStairs0(self, n: int) -> int:
        import math
        sqrt5=5**0.5
        fibin=math.pow((1+sqrt5)/2,n+1)-math.pow((1-sqrt5)/2,n+1)
        return int(fibin/sqrt5)

