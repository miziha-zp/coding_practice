```python
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        record = {}
        for i in arr:
            if i in record:
                record[i] += 1
            else:
                record[i] = 1
        cnt = []
        for i in record:
            cnt.append(record[i])

        cnt = sorted(cnt)[::-1]

        ans = 0
        acc = 0
        for  i in cnt:
            ans += 1
            acc += i
            if acc >= len(arr) // 2:
                return ans
```