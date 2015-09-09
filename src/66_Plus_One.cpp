class Solution {
public:
    vector<int> plusOne(vector<int> &dig) {
        vector<int> ans;
        bool k = true;
        for(int i = dig.size()-1 ; i>=0;i--){
            if(dig[i] == 9 && k) ans.push_back(0);
            else if(k){
                k = false;
                ans.push_back(dig[i] + 1);
            }else{
                ans.push_back(dig[i]);
            }
        }
        if(k) ans.push_back(1);
        reverse(ans.begin(),ans.end());
        return ans;
    }
};