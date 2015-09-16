class Solution {
private:
    vector<vector<int> > vvi;
    void depth(TreeNode *root,int dep) {
        if(vvi.size() < dep + 1) vvi.push_back(vector<int>());
        if(root){
            vvi[dep].push_back(root->val);
            depth(root->left,dep+1);
            depth(root->right,dep+1);
        }else{
            vvi[dep].push_back(-1);
        }
    }
public:
    bool isSymmetric(TreeNode *root) {
        bool k = true;
        depth(root,0);
        for(auto i = 1;i<vvi.size() && k;i++){
            if(vvi[i].size() % 2 == 1) k = false;
            for(auto j = 0;j<vvi[i].size()/2 && k;j++){
                if(vvi[i][j] != vvi[i][vvi[i].size() - j -1]) k = false;
            }
        }
        return k;
    }
};