T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().strip().split()))

    ans = 0
    dp = {}
    dp[-1] = 0
    for i, a in enumerate(A):
        if a == 0:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
    
    for i in range(n):
        for j in range(i, n):
            ans += (j - i + 1) + (dp[j] - dp[i - 1])
    
    print(ans)