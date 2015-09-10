class Solution {
private:
    int fun(string a){
        int ans = 0;
        for(int i=0;i<a.size();i++)
            ans = ans*2 + a[i] - '0';
        return ans;
    }
public:
    string addBinary(string a, string b) {
        if(a.size() < b.size()) return addBinary(b,a);
        string s;
        int digA = a.size()-1,digB = b.size() - 1,up = 0;
        while(digB >=0){
            int now = up + a[digA] - '0' + b[digB] - '0';
            s.push_back(now % 2 + '0');
            up = now / 2;
            digA--;digB--;
        }
        while(digA>=0){
            int now = up + a[digA] - '0';
            s.push_back(now % 2 + '0');
            up = now / 2;
            digA--;
        }
        if(up) s.push_back('1');
        reverse(s.begin(),s.end());
        return s;
    }
};