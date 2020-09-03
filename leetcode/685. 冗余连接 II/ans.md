```python
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        record = list(range(0,len(edges)+1))
        # def getroot(n):
        #     if record[n] != n:
        #         record[n] = getroot(n);
        #     return record[n];
        # recursion may lead to depth exceed.

        def getroot(n):
            temp = []
            while(record[n]!=n):
                temp.append(n)
                n = record[n]
            for i in temp:
                record[i] = n
            return n
        node = 0
        count = [0] * (len(edges) + 1)
        for edge in edges:
            count[edge[1]] += 1
            if count[edge[1]] == 2:
                node = edge[1]

        for edge in edges:
            l,r = getroot(edge[0]),getroot(edge[1])
            if edge[1] == node:
                continue
            if l == r:
                return edge
            else:
                record[r]=l
    
        for edge in edges:
            if edge[1] != node:
                continue
            l,r = getroot(edge[0]),getroot(edge[1])
            if l == r:
                return edge
            else:
                record[r]=l

```