```C++
class Solution {
public:
    vector<int> singleNumbers(vector<int>& nums) {
        int res = 0;
        for (int num:nums){
            res ^= num;
        }
        int h = 1;
        while((h & res) == 0){
            h = h << 1;
        }
        int a =0, b = 0;
        for (int num:nums){
            if(h&num){
                a ^= num;
            }
            else{
                b ^= num;
            }
        }
        vector<int>ans(2);
        ans[0] = a;
        ans[1] = b;
        return ans;
    }
};
```