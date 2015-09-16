class Solution {
public:
    vector<vector<int> > generate(int n) {
        vector<vector<int> > vvi;
        for(int i=0;i<n;i++){
            vector<int> vi;
            for(int j=0;j<=i;j++){
                if(j>0 && j<i) vi.push_back(vvi[i-1][j-1] + vvi[i-1][j] );
                else vi.push_back(1);
            }
            vvi.push_back(vi);
        }
        return vvi;
    }
};