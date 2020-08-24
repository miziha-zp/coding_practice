```C++
class Solution {
public:
    int cuttingRope(int n) {
        int ans[58] = {0};
        ans[1] = 1;
        for(int i=2;i<=n;i++){
            for(int j=1;j<i;j++){
                ans[i] = max(ans[i],ans[j]*ans[i-j]);
                ans[i] = max(ans[i],ans[j]*(i-j));
                ans[i] = max(ans[i],j*ans[i-j]);
                ans[i] = max(ans[i],j*(i-j));
            }
        }
        return ans[n];
    }
};
```