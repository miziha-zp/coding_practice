```C++
class Solution {//经典的线性DP。
public:
    int maxValue(vector<vector<int>>& grid) {
        int m = grid[0].size();
        int n = grid.size();
        int ans[200] = {0};
        for(int i=0;i<n;i++){
            ans[0] = ans[0] + grid[i][0];
            for (int j=1;j<m;j++){
                ans[j] = max(ans[j] + grid[i][j],ans[j-1] + grid[i][j]);
            }
        }
        return ans[m-1];
    }
};
```