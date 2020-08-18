```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int get_depth(TreeNode* root){
        if (root == NULL)
            return 0;
        int left =  root->left ? get_depth(root->left) : 0;
        int right = root->right ? get_depth(root->right) : 0;
        return 1 + max(left,right);
    }
    bool isBalanced(TreeNode* root) {
        if (!root||(root->left == NULL && root->right == NULL))
            return true;
        return isBalanced(root->left)&&
                isBalanced(root->right)&&
                abs(get_depth(root->left) - get_depth(root->right)) <= 1;
    }
};
```