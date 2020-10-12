class Solution {
public:
    int fib(int N) {
        if (N == 0){
            return 0;
        }
        if(N == 1 || N == 2){
            return 1;
        }
        int res[2] = {1,1};
        int i = 2;
        while (i < N){
            int flag = i % 2;
            res[flag] = res[0] + res[1];
            i += 1;
        }
        return res[(i-1) % 2];

    }
};