class Solution {
private:
    vector<vector<int> > vvi;
    void depth(TreeNode *root,int dep) {
        if(root){
            if(vvi.size() < dep + 1) vvi.push_back(vector<int>());
            vvi[dep].push_back(root->val);
            depth(root->left,dep+1);
            depth(root->right,dep+1);
        }
    }
public:
    vector<vector<int> > levelOrder(TreeNode *root) {
        depth(root,0);
        return vvi;
    }
};