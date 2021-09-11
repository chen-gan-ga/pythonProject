# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
#


# 输入:
s = "anagram"
t = "nagaram"
# 输出: true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #特判断
        if len(s)!=len(t):return False
        #哈希
        dic0={}
        dic1={}
        for i in range(len(s)):
            if s[i] in dic0:
                dic0[s[i]]=dic0[s[i]]+1
            else :
                dic0[s[i]]=1
            if t[i] in dic1:
                dic1[t[i]]=dic1[t[i]]+1
            else :
                dic1[t[i]]=1
        for key in dic0:
            if key not in dic1:return False
            elif dic0[key]!=dic1[key]:return False
        return True

answer=Solution()
print(answer.isAnagram(s,t))



