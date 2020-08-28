```//多容量限制的背包
class Solution {
public:
    int count0(string t){
        int cnt = 0;
        for(char c:t){
            if(c == '0'){
                cnt++;
            }
        }
        return cnt;
    }
    int findMaxForm(vector<string>& strs, int m, int n) {
        // int ans = 0;
        int dp[101][101] = {0};
        int maxANS = 0;
        for(string str:strs){
            int _0 = count0(str);
            int _1 = str.size() - _0;
            for(int i = m; i >=  _0; i--){
                for(int j = n; j>= _1; j--){
                    dp[i][j] = max(dp[i][j],dp[i - _0][j - _1] + 1);
                    maxANS = max(dp[i][j],maxANS);
                }
            }
        }

        return maxANS;
    }
};
```