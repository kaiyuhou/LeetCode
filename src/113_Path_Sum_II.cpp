class Solution {
private:
    bool k;
    vector<vector<int> > routeList;
    void check(TreeNode *root, int sum,int now,vector<int> route){
        if(root == NULL) return;
        if(now + root -> val == sum && root -> left == NULL && root -> right == NULL){
            route.push_back(root->val);
            routeList.push_back(route);
        }
        route.push_back(root->val);
        check(root->left,sum, now + root -> val, route);
        check(root->right,sum, now + root -> val, route);
    }
public:
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        vector<int> route;
        check(root,sum,0,route);
        return routeList;
    }
};