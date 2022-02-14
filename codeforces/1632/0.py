T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().strip().split()))
    for i in range(1, n):
        if A[i] < A[i-1]:
            print("YES")
            break
    else:
        print("NO")
    
