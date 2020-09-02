```python
class Solution:
    def waysToStep(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(1, n):
            dp[0], dp[1], dp[2] = dp[1], dp[2], (dp[0] + dp[1] + dp[2]) % 1000000007
        return dp[2]
```