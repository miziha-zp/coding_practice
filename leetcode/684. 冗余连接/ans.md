```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        record = list(range(0,len(edges) + 1))
        def get_f(n):
            if record[n] == n:
                return n
            else:
                record[n] = get_f(record[n])
                return record[n] 
        for edge in edges:
            l,r = get_f(edge[0]),get_f(edge[1])
            if l==r:
                return edge
            else:
                record[l] = r

```
