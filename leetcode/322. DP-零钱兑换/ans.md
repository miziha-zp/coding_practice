```C++ // 完全背包
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int maxsize = amount + 1;
        vector<int>ans(maxsize,maxsize); // 用maxsize初始化，解决没有解的情况
        ans[0] = 0;
        for (int i=0;i<coins.size();i++){
            for(int j=coins[i];j<=amount;j++){
                ans[j] = min(ans[j],ans[j-coins[i]]+1);
            }
        }
        return ans[amount] > amount ? -1 : ans[amount];
    }
};
```