from typing import List

numbers = [2,3,4]
target = 6
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        while target >numbers[i]:
            while numbers[i]==numbers[i+1]:i=i+1
            j=i+1
            while target >=numbers[j]:
                if numbers[j]+numbers[i]==target:
                    return [i,j]
                j=j+1
            i=i+1


ans=Solution()
print(ans.twoSum(numbers,target))