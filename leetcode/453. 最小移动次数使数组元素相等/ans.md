```python
'''
脑经急转歪,每天一到智力题,健康生活100岁
'''
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)
```