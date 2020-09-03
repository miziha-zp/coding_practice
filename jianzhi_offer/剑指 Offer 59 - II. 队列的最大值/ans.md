```python
import queue
class MaxQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()
    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        self.queue.put(value)
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        value = self.queue.get()
        if value == self.deque[0]:
            self.deque.popleft()
        return value
# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
```

判断队列为空不要使用queue，原因如下：

```python
>>> import queue
>>> a = queue.Queue()
>>> not a
False
```
Queue的操作：
Queue.get()
Queue.put()
Queue.empty()
Queue.full()

deque的操作：
deque.append()
deque.pop()
deque.popleft()
deque.clear()
not deque 判断双端队列非空

