class Solution {
private:
    bool k;
    void check(TreeNode *root, int sum,int now){
        if(k) return;
        if(root == NULL) return;
        if(now + root -> val == sum && root -> left == NULL && root -> right == NULL){
            k = true;
        }
        check(root->left,sum, now + root -> val);
        check(root->right,sum, now + root -> val);
    }
public:
    bool hasPathSum(TreeNode *root, int sum) {
        k = false;
        check(root,sum,0);
        return k;
    }
};