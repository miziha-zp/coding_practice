```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        def get_str(prex):
            if len(prex) == 0:
                return ""
            ans = str(prex[0])
            for i in range(1,len(prex)):
                ans += "->"
                ans += str(prex[i])
            return  ans
            # return "->".join(prex) 不支持这个操作
        def dfs(root,prex):
            if not root.right and not root.left:
                ans.append(get_str(prex))
                return 
            if root.left:
                prex.append(root.left.val)
                dfs(root.left,prex)
                prex.pop()
            if root.right:
                prex.append(root.right.val)
                dfs(root.right,prex)
                prex.pop()
        if not root:
            return []
        dfs(root,[root.val])
        return  ans
```