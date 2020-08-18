**此题虽然简单，面试遇到时一定要向面试官询问是否可以修改nums数组！！！**
```C++
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        for (int i=1;i<nums.size();i++){
            nums[i] += nums[i-1];
        }
        return nums;
    }
};
```