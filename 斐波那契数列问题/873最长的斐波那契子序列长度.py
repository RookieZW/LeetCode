
# 如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：

# n >= 3
# 对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
# 给定一个严格递增的正整数数组形成序列，找到 A 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。

# （回想一下，子序列是从原序列 A 中派生出来的，它从 A 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）

#  

# 示例 1：

# 输入: [1,2,3,4,5,6,7,8]
# 输出: 5
# 解释:
# 最长的斐波那契式子序列为：[1,2,3,5,8] 。

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        n = len(A)
        result = 0
        
        for i in range(n-1):
            for j in range(i+1, n):
                a, b = A[i], A[j]
                count = 2
                while a+b in s:
                    a, b = b, a+b
                    count += 1
                    result = max(result, count)
        return result if result > 2 else 0