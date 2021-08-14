m = [0, 2, 0, 0, 0, 0, 1, 2, 0, 5, 0, 0]

class MoveZeroes(object):
    def solution1(self,nums):
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                del (nums[i])
                nums.append(0)

    def solution2(self,nums):
        index = 0
        for i in range(len(nums)):  # 第一次循环，先把所有非零元素前移
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        for i in range(index, len(nums)):  # 第二次循环，把后面补上0
            nums[i] = 0

    def solution3(self,nums):
        j = 0
        for i in range(len(nums)):
            # 当前元素!=0，就把其交换到左边，等于0的交换到右边
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums

shucu= MoveZeroes()
print(shucu.solution3(m))
print('测试上传')