
class Solution {
public:
    void merge(int A[], int m, int B[], int n) {
        int tail = m + n - 1,pB = n - 1, pA = m -1;
        while(pA >= 0 && pB >= 0){
            if(A[pA] > B[pB]){
                A[tail] = A[pA];
                pA--;
            }else{
                A[tail] = B[pB];
                pB--;
            }
            tail--;
        }
        if(pB >= 0){
            for(int i=0;i<=pB;i++){
                A[i] = B[i];
            }
        }
    }
};