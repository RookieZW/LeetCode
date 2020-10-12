'''
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

 

示例 1：

输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-th-tribonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution {
public:
    int tribonacci(int n) {
        int res[3] = {1,1, 2};
        if (n == 0)
            return 0;
        else if (n == 1 || n == 2)
            return 1;
        else if (n == 2)
            return 2;
        else{
            for (int i = 3; i < n; i++){
                int flag = i % 3;
                res[flag] = res[0] + res[1] + res[2];
            }
            return res[(n - 1) % 3];
        }
    }
};
