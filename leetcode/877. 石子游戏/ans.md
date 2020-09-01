```c++
class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        int dp[550] = {0};
        for(int i=piles.size();i>=1;i--){
            dp[i] = piles[i-1];
            for(int j=i+1;j<=piles.size();j++){
                dp[j] = max(piles[i-1] - dp[j],piles[j-1] - dp[j-1]);
            }
        }

        return dp[int(piles.size())] > 0;
    }
};
```
数学上可以证明先手存在必胜策略，并且可以给出必胜策略，可以直接返回true。