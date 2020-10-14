/*
有K个egg
N层楼
确定那一层恰好不会摔破鸡蛋（高一层破）
*/

class Solution {
    public int superEggDrop(int K, int N) {
        int[][] res = new int[K+1][N+1];
        int m = 0;
        while(res[K][m] < N){
            m++;
            for (int k = 1; k <= K; k++){
                res[k][m] = res[k][m-1]+res[k-1][m-1]+1;
            }
        }
        return m;

    }
}

/*
	DP[K][M] = DP[K-1][M-1]+DP[K][M-1]+1
*/