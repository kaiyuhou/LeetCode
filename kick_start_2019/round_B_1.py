from math import *
t = int(input())
for T in range(1, t + 1):
    N, Q = [int(s) for s in input().split(" ")]
    S = input()
    dp = []
    for i in range(26):
        dp.append([0])

    for a in range(1, N + 1):
        for i in range(26):
            dp[i].append(dp[i][a - 1])
        dp[ord(S[a - 1]) - ord('A')][-1] += 1

    ans = 0
    for _ in range(Q):
        L, R = [int(s) for s in input().split(" ")]
        nodd = 0
        for i in range(26):
            if (dp[i][R] - dp[i][L - 1]) % 2 == 1:
                nodd += 1
        if nodd < 2:
            ans += 1

    print("Case #{}: {}".format(T, ans))