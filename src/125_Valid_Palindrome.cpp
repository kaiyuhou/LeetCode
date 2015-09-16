class Solution {
private:
    char lowCase(char c){
        if(c>='A' && c<='Z')
            return c + ('a' - 'A');
        else return c;
    }
    bool isAlphaNum(char c){
        if((c>='A' && c<='Z') || (c>='0' && c <='9') || (c>='a' && c<='z'))
            return true;
        else return false;
    }
public:
    bool isPalindrome(string s) {
        int n = (int)s.size() - 1,i=0;
        bool k = true;
        while(i < n){
            while(i < n && isAlphaNum(s[i]) == false){
                i++;
            }
            while(n > i && isAlphaNum(s[n]) == false){
                n--;
            }
            //cout<<i<<" "<<s[i]<<" "<<n<<" "<<s[n]<<endl;
            if(i < n){
                if( lowCase(s[i]) != lowCase(s[n])){
                    k = false ;
                    break;
                }
            }
            i++;
            n--;
        }
        return k;
    }
};