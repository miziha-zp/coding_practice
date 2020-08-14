```c++
//参考了官方题解：https://leetcode-cn.com/problems/qiu-12n-lcof/solution/qiu-12n-by-leetcode-solution/
class Solution {
public:
    int sumNums(int n) {
        int sum = n;//n = 1e4时，sum<1e9
        n && (sum += sumNums(n-1));//&&实现短路操作，模拟if n == 0 return 
        return sum;
    }
};

```

```python
class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(range(1,n+1))
```