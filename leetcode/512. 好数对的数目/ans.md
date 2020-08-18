```C++
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int record[101] = {0};
        int ans = 0;
        for(int num:nums){
            ans += (record[num]++);
        }
        return ans;
    }
};
```
```python
class Solution(object):
    def Ndel1sum(self,n):
        # return sum(range(n))
        return n * (n-1) // 2

    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        frequency_record = {}
        for i in nums:
            if i in frequency_record:
                ans += frequency_record[i]
                frequency_record[i] += 1 
            else:
                frequency_record[i] = 1
        return ans
```