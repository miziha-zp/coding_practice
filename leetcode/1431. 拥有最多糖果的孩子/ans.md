```python # 害，刷这道题，恭喜你浪费生命中的五分钟。
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandiesValues = max(candies)
        return [extraCandies + candies[i] >= maxCandiesValues for i in range(len(candies))]
```