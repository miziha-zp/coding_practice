```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        openroom = [1] + [0] * 1000
        curopen = 1
        keylist = [0]
        while 1:
            t_list = []
            sz = len(keylist)
            for i in range(sz):
                for key_ in rooms[keylist[i]]:
                    if openroom[key_] == 1:
                        continue
                    else:
                        openroom[key_] = 1
                        t_list.append(key_)
            keylist = t_list

            if curopen == sum(openroom):
                return curopen == len(rooms)
            curopen = sum(openroom)
```