```C++ //课本上的区间DP
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans = nums[0];
        int cur = ans;
        for(int i=1;i<nums.size();i++){
            cur = cur > 0 ? cur + nums[i] : nums[i]; 
            ans = max(ans,cur);
        }
        return ans;
    }
};
```