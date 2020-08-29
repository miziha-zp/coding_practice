```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for i in nums:
            ans += [j+[i]for j in ans]
        return ans
```

```C++ 
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        ans.push_back({});
        for(int num:nums){
            int sz = ans.size();//注意vector动态增长，不要for(vector<int>temp:ans) 
            for(int j=0;j<sz;j++){
                vector<int>temp(ans[j].begin(),ans[j].end());
                temp.push_back(num);
                ans.push_back(temp);
            }
        }
        return ans;
    }
};
```