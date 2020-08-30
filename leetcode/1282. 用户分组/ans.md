```python
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        record = {}
        for index,i in enumerate(groupSizes):
            if i in record:
                record[i].append(index)
            else:
                record[i] = [index]
        
        ans = []

        for i in record:
            candiate = record[i]
            for j in range(len(candiate) // i):
                ans.append(candiate[j*i:i*(j+1)])
        
        return ans

```
