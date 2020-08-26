```python
class Solution:
    def waysToChange(self, n: int) -> int:
        ans = [0] * (n + 1)
        ans[0] = 1
        mod = 1000000007
        for coin in [1,5,10,25]:
            for m in range(coin,n+1):
                ans[m] += ans[m - coin];

        return ans[n] % mod
```