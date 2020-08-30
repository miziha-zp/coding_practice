```python
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x:(-x[0],x[1]))
        ans = []
        for i in people:
            ans.insert(i[1],i)
        return ans
```

```C++
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        vector<vector<int>> ans;
        sort(people.begin(),people.end(),[](auto a,auto b){return a[0]==b[0]?a[1]<b[1]:a[0]>b[0];});
        for(auto p:people){
            ans.insert(ans.begin()+p[1],p); // 变长插入，用迭代器+坐标
        }
        return ans;
    }
};
```