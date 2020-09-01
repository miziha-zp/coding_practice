```python
# DFS
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def getmax(start,end,turn):
            if start == end:
                return nums[start] * turn
            pickleft = turn * nums[start] + getmax(start + 1,end,turn * -1)
            pickright = turn * nums[end] + getmax(start,end-1,turn * -1)
            return max(pickleft*turn,pickright*turn) * turn
        return getmax(0,len(nums)-1,1) >= 0
```
```C++
// DP
class Solution {
public:
    bool PredictTheWinner(vector<int>& nums) {
        int dp[29] = {0};
        for(int i=nums.size();i>=1;i--){
            dp[i] = nums[i-1];
            for(int j=i+1;j<=nums.size();j++){
                dp[j] = max(nums[i-1]-dp[j],nums[j-1]-dp[j-1]);
            }
        }
        return dp[int(nums.size())] >= 0;
    }
};

```