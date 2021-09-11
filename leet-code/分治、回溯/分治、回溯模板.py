# 1.泛型递归
def recursion(leve,p1,p2):
    if leve>max_leve:
        process_result
        return

    process(leve,data)

    self.recursion(leve+1,p1,p2)

    #清理状态

# 2.分治代码模板
def divide_conquer(problem,p1,p1):
    #没有问题需要解决了 停止
    if problem is None:
        print_result
        return

    # prepare data
    #拆解子问题：比如n的阶乘 就是n*fac(n-1)
    #斐波拉切：就是n-1、n-2的递归结果
    #左右括号：分别存左括号、右括号存起来
    data=prepare_data(problem)
    subproblems= split_problem(problem,data)
    #conquer subproblems
    #下探一层，解决更细节的问题
    subresult1=self.divide_conquer(subproblems[0],p1,p2)
    subresult2=self.divide_conquer(subproblems[1],p1,p2)
    subresult3=self.divide_conquer(subproblems[2],p1,p2)

    #process and generate the final result
    result = process_result(subresult1,subresult2,subresult3)