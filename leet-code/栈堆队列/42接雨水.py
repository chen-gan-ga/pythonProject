from typing import List

height=[0,1,0,2,1,0,1,3,2,1,2,1]
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        temp_h = 0
        while left <= right:
            min_l_f = min(height[left], height[right])
            if min_l_f > temp_h:
                result += (min_l_f-temp_h) * (right - left + 1)
                temp_h = min_l_f
            while left<=right and height[left] <= temp_h:
                left += 1
            while left<=right and height[right] <= temp_h:
                right -= 1
        result = result-sum(height)
        return result

# 作者：ywh1998
# 链接：https://leetcode-cn.com/problems/trapping-rain-water/solution/shuang-zhi-zhen-85-55-by-ywh1998/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

answer=Solution()
print(answer.trap(height))