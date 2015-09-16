class Solution {
private:
    bool k;
    void depth(TreeNode *p, TreeNode *q) {
        if(!k) return;
        if(p && q){
            if(p->val == q->val){
                depth(p->left,q->left);
                depth(p->right,q->right);
            }else k = false;
        }else if(p || q) k = false;
    }
public:
    bool isSameTree(TreeNode *p, TreeNode *q) {
        k = true;
        depth(p,q);
        return k;
    }
};