T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().strip().split()))

    ans = 0
    one = 0
    for i in range(1, n - 1):
        ans += (A[i] + 1) // 2
        if A[i] == 1:
            one += 1
    if one >= n - 2:
        print(-1)
    elif n == 3 and A[1] % 2 == 1:
        print(-1)
    else:
        print(ans)  
    