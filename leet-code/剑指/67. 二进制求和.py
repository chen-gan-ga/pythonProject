# 输入:
a = "1010"
b = "1011"
# 输出: "100"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aa,bb,res=[],[],''

        weiba=0
        level=0
        lenn=max(len(a),len(b))
        for i in range(len(a)):
            aa.append(int(a[i]))
        for i in range(len(b)):
            bb.append(int(b[i]))
        while level<lenn+2:
            level=level+1
            if aa or bb or weiba==1:
                if aa:
                    aa1 = aa[-1]
                    del aa[-1]
                else:
                    aa1 = 0

                if bb:
                    bb1 = bb[-1]
                    del bb[-1]
                else:
                    bb1 = 0

                if aa1 + bb1 + weiba == 0:
                    res = '0' + res
                    weiba = 0
                elif aa1 + bb1 + weiba == 1:
                    res = '1' + res
                    weiba = 0
                elif aa1 + bb1 + weiba == 2:
                    res = '0' + res
                    weiba = 1
                else:
                    res = '1' + res
                    weiba = 1
        return res




ans=Solution()
ans.addBinary(a,b)