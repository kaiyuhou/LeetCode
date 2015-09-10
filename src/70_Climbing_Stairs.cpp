class Solution {
private:
    int f(int n){
        int last = 1, now = 1;
        for(int i=3;i<=n;i++){
            now += last;
            last = now - last;
        }
        return now;
    }
public:
    int climbStairs(int n) {
        if(n == 0) return 0;
        else if(n == 1) return 1;
        else if(n == 2) return 2;
        else if(n == 3) return 3;
        else return f(n - 2)*3 + f(n - 3)*2;
    }
};