'''
给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。

斐波那契数字定义为：

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 ， 其中 n > 2 。
数据保证对于给定的 k ，一定能找到可行解。

 

示例 1：

输入：k = 7
输出：2 
解释：斐波那契数字为：1，1，2，3，5，8，13，……
对于 k = 7 ，我们可以得到 2 + 5 = 7 。
'''
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        count = 0
        res = [1,1]
        if k == 0:
            return 0
        elif k == 1:
            return 1
        
        while res[-1] <= k:
            res.append(res[-1]+res[-2])
        
        length = len(res) - 1

        for i in range(length, -1, -1):
            if k > res[i]:
                count += 1
                k -= res[i]
            elif k == res[i]:
                if i ==0:
                    return count
                return count + 1
        return 0

'''
先计算斐波那契数列
再计算最小数（DP）但是我没用 
	DP = [1,2,3。。。]
	转移方程为
	min(DP[i], DP[[i - x]]+1])
'''
