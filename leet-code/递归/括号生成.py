# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
# 有效括号组合需满足：左括号必须以正确的顺序闭合。
#
#  
#
# 示例 1：
#
# 输入：
from typing import List

n = 3


class Solution:
    def generateParenthesis(self, n) :
        res=[]


        def recursion(now,n,s):
            # 递归终结条件
            if now>=2*n:
                res.append(s)
                return
            # process logic in current level/处层当前层逻辑
            s1=s+'('
            s2=s+')'

            # drill down/下探至下一层
            recursion(now+1,n,s1)
            recursion(now+1,n,s2)

        recursion(0,n,'')
        return res

    def generateParenthesis0(self, n):
        res = []
        def recursion(left,right,n,s):
            if left+right>=2*n:
                res.append(s)
                return
            if left<n:
                recursion(left+1,right,n,s+'(')


            if right<left:
                recursion(left, right+1, n, s+')')

        recursion(0,0,n,'')
        return res



ans=Solution()
print(ans.generateParenthesis0(3))
