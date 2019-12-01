from math import *
t = int(input())
for T in range(1, t + 1):
    N, S = [int(s) for s in input().split(" ")]
    M = [set() for _ in range(S)]
    P = [[] for _ in range(N)]
    for i in range(N):
        SS= [int(s) - 1 for s in input().split(" ")]
        SS.pop(0)
        for s in SS:
            M[s].add(i)
            P[i].append(s)

    ans = 0
    for i in range(N):
        temp = set()
        for j, m in enumerate(M):
            if j in P[i]: continue
            temp |= m
        # print(i, temp)
        ans += len(temp)

    print("Case #{}: {}".format(T, ans))