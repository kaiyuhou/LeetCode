class Solution {
private:
    bool k;
public:
    bool isBalanced(TreeNode *root) {
        k = true;
        depth(root);
        return k;
    }
    int depth(TreeNode *root) {
        if(root){
            if(!(root->left || root->right)) return 1;
            int l = depth(root->left) + 1;
            int r = depth(root->right) + 1;
            if(abs(l-r) > 1) k = false;
            return l>r?l:r;
        }
        return 0;
    }
};