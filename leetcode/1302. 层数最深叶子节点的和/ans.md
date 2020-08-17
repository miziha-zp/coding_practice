```python DFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0
        self.max_depth = 0
    def getMaxDepth(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + max(self.getMaxDepth(root.left),self.getMaxDepth(root.right))
    def dfs(self,root,depth):
        if not root.left and not root.right:
            if depth == self.max_depth:
                self.ans += root.val;
            return;
        if root.left:
            self.dfs(root.left,depth+1)
        if root.right:
            self.dfs(root.right,depth+1)   

    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = self.getMaxDepth(root);
        self.dfs(root,1)
        return self.ans;
```
