#Recursion 递归
# 计算 n！
def Fac(n):
    #终止条件/recursion terminator
    if n<=1:
        return n
    return n*Fac(n-1)
print(Fac(5))

# 模板
def recursion(leve,param1,param2):
    #递归终结条件
    if leve>Max_level:
        process_result
        return
    #process logic in current level/处层当前层逻辑
    process(leve,data....)

    #drill down/下探至下一层
    self.recursion(leve+1,p1,...)

    #清理当前层

