```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([t_str[::-1]for t_str in s.split()])
```