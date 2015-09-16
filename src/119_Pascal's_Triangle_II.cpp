class Solution {
public:
    vector<int> getRow(int n) {
        vector<int> vi;
        vi.push_back(1);
        for(int i=1;i<=n;i++){
            vi.push_back(  (int) ((long long)vi[i-1] * (n-i+1)/i));
        }
        return vi;
    }
};