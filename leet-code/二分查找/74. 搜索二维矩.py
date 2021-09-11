# 74. 搜索二维矩阵
from typing import List

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #首先确定在哪个矩阵范围中：
        ll,rr=0,len(matrix)-1

        while ll<=rr:
            mid=(ll+rr)//2
            if target>=matrix[mid][0] and target<=matrix[mid][-1]:
                l1,r1=0,len(matrix[mid])-1

                while l1<=r1:
                    mid1=(l1+r1)//2
                    if  target==matrix[mid][mid1]:return True
                    elif target>matrix[mid][mid1]:l1=mid1+1
                    else:r1=mid1-1
                return False
            elif target<matrix[mid][0]:
                rr=mid-1
            else:ll=mid+1
        return False

ans=Solution()
print(ans.searchMatrix(matrix,target))

