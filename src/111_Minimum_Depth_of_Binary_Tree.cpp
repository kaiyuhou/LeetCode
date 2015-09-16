class Solution {
public:
    int minDepth(TreeNode *root) {
        if(root){
            if(!(root->left || root->right)) return 1;
            int l=0x3fff,r=0x3fff;
            if(root->left) l = minDepth(root->left) + 1;
            if(root->right) r =  minDepth(root->right) + 1;
            return l>r?r:l;
        }
        return 0;
    }
};