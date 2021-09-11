# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#
# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母都恰好只用一次。
#
# 示例 1:

# 输入:\
import collections
from typing import List
from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsNew=[]
        dic=collections.defaultdict(list)
        for i in range(len(strs)):
            tem=list(strs[i])
            tem.sort()
            strsNew.append("".join(tem))
        for i in range(len(strsNew)):
            dic[strsNew[i]].append(strs[i])
        return list(dic.values())


    def bestGroupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())



answer=Solution()
print(answer.bestGroupAnagrams(strs))
